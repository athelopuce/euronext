# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
from flask import request, flash, url_for, redirect, render_template
from .. import db
from ..models import Ord, Act
from . import main
from .forms import MyForm, NewAct, NewOrd
from flask import jsonify  # pour route interactive
# import requests  # pour page newAct delete '/foo'
# import time  # for test1 addnumber

# import logging

from datetime import datetime  # temp. à placer dans des fonctions personnels


@main.route('/homeTest')
def homeTest():
#    return "Hello, World!"
    form = MyForm()
    print(url_for('.index'))
    return render_template('main/index.html',
                           form=form
                           )


@main.route('/')
@main.route('/index')
def index():
#    return "Hello, World!"
    form = MyForm()
    print('url_for: ', url_for('.index'))
    q = db.session.query(Act)
    print('session: ', db.session.query(q.exists()))
#    q = Act.query.all()  # dict() of Act
    q = db.session.query(Act).order_by(Act.name.asc())
    for u in q:
        print(u.__dict__)
    if q is None:
        return render_template('main/index.html', form=form)
    else:
        return render_template('main/index.html', form=form, listActions=q)


#    return render_template(url_for('.index'),
#                           form=form,
#                           listActions=Act.query.all())
#    return render_template('index.html',
#                           form=form, name=session.get('name'),
#                           known=session.get('known', False),
#                           listActions=Act.query.all())


# new Version faire newAct pour ajouter action
@main.route('/newAct', methods=['GET', 'POST', 'DELETE'])
def newAct():
    form = NewAct()
    q = Act.query.order_by(Act.name).all()

#    if form.validate_on_submit():
#        act = Act(name=form.name.data, symbol=form.symbol.data)
#        db.session.add(act)
#        db.session.commit()
#        flash('Congratulations, action was successfully added!')
#        return redirect(url_for('.index'))  # or main.index
#    elif request.method == 'DELETE':
#        # Retrieve data from the request and remove it from the database
#        myId = request.form.get('column1')
#        print(myId)
#        print(nameid)
#        print('ok')

    return render_template('main/newAct.html',
                           title='newAct', form=form,
                           listActions=q)


# with ajax et newAct
@main.route("/delRow", methods=["POST"])
def delRow():
    i = request.form.get("id", type=int)
    t = request.form.get("table", type=str)  # table
#    act = Act.query.filter_by(idAct=i).first()
    print('i:', i, ' t:', t)
    if i < 0:
        print('Exit delRow')
        return jsonify(result='pas de data')
    if t == 'newAct':
        item = Act.query.get(i)  # get idAct
        print('item:', item)
        if item is None:
            return jsonify(ida=i, result='pas de data')
#        n = request.form.get("name", type=str)  # à effacer
        db.session.delete(item)
        db.session.commit()
        flash('Congratulations, stock {} deleted!'.format(
                item.name), 'success')
        return jsonify(ida=i, name=item.name)
    if t == 'newOrd':
        item = Ord.query.get(i)  # get idAct
        if item is None:
            return jsonify(ido=i, result='pas de data')
        db.session.delete(item)
        db.session.commit()
        flash('Congratulations, order {} deleted!'.format(
                item.idOrd), 'success')
        return jsonify(ido=i, sens=item.sens)


# with ajax et newAct
@main.route("/editRow", methods=["POST"])
def editRow():
    i = request.form.get("id", type=int)
    t = request.form.get("table", type=str)  # table
    print('i:', i, ' t:', t)
    if t == 'newAct':
        n = request.form.get("name", type=str)
        s = request.form.get("symbol", type=str)
        # recherche par id
        item = Act.query.get(i)  # get idAct
        # Recherche par nom
#        item = db.session.query(Act).filter_by(name=n, symbol=s).first()
        print('item:', item)
        if item is None:
            # add new action
            act = Act(name=n, symbol=s)
            db.session.add(act)
            db.session.commit()
            i = act.idAct
            print('Return new id Act value %s\n' % act.idAct)
            flash('New stock {}, added!'.format(
                act.name), 'success')
        else:
            # update action
            flash('New stock {}, updated!'.format(
                item.name), 'success')
            item.name = n
            item.symbol = s
            db.session.commit()
        return jsonify(ida=i, name=n, symbol=s)
    if t == 'newOrd':
        # sens, date, PriceAchat, quantity, idAct
        s = request.form.get("sens", type=str)
        d = request.form.get("ordDate")
        px = request.form.get("PriceAchat", type=float)
        qt = request.form.get("quantity", type=int)
        ida = request.form.get("idAct", type=int)
        item = Ord.query.get(i)  # get idAct
        print('item:', item)
        if item is None:
            # add new order NON utilisé voir form newOrd
            print('date:', type(d), d)
            ord_ = Ord(sens=s, ordDate=d, PriceAchat=px, quantity=qt,
                       idAct=ida)
            db.session.add(ord_)
            db.session.commit()
            i = ord_.idOrd
            print('Return new id Act value %s\n' % ord_.idOrd)
            flash('New order {} de {} {}, added!'.format(
                ord_.sens, ord_.quantity, ord_.idAct), 'success')
        else:
            # update action
            flash('New order {}, updated!'.format(
                item.idOrd), 'success')
            item.sens = s
            print('date1:', type(d), d)
            date_ord = datetime.strptime(d, '%d/%m/%Y').date()
            print('date2:', type(date_ord), date_ord)
            # format='%d/%m/%Y' date: <class 'datetime.date'> 2020-02-10
            item.ordDate = date_ord
            item.PriceAchat = px
            item.quantity = qt
            item.idAct = ida
            db.session.commit()
        return jsonify(ido=i, sens=s, ordDate=d, PriceAchat=px, quantity=qt,
                       idAct=ida)


# a Revoir
@main.route('/newEdit', methods=['GET', 'POST'])
def newEdit():
    form = NewAct()
    if request.method == 'POST' and form.validate():
        act = Act(
                name=form.name.data,
                symbol=form.symbol.data
                )
        db.session.add(act)
        db.session.commit()
        flash('New stock {}, added!'.format(
                    act.name), 'success')
        return redirect(url_for('.index'))  # or main.index
    elif request.method == 'GET':
        # Retrieve data from the request and remove it from the database
        myId = request.form.get('column1')
        print(myId)
#        print(nameid)
        print('ok')
    return render_template('newEdit.html',
                           title='newEdit', form=form,
                           listActions=Act.query.all())


# table des ordres passés
@main.route('/newOrd', methods=['GET', 'POST', 'DEL'])
def newOrd():
    form = NewOrd()
    available_act = Act.query.all()
    # Now forming the list of tuples for SelectField
    groups_act = [(i.idAct, i.name) for i in available_act]
    form = NewOrd(request.form)  # form = NewOrd(request.form)
    # passing groups_act to the form
    form.idAct.choices = groups_act
    print('form1: %s' % form.validate())
    print('form2: %s' % form.validate_on_submit())
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.sens.data)
            print('sens: %s' % form.sens.data)
            print('ordDate: %s' % form.ordDate.data)
            print('quantity: %d' % form.quantity.data)
            print('idAct: %d' % form.idAct.data)
            print('PriceAchat: %s' % form.PriceAchat.data)
            print('Type(ordDate):', type(form.ordDate.data), form.ordDate.data)
            ord_ = Ord(
                    sens=form.sens.data,
                    ordDate=form.ordDate.data,
                    PriceAchat=form.PriceAchat.data,
                    quantity=form.quantity.data,
                    idAct=form.idAct.data
                    )
            db.session.add(ord_)
            db.session.commit()
            print(ord_)
            flash('New order, {}, added!'.format(
                    ord_.idAct), 'success')
            return redirect(url_for('.index'))  # or main.index
        else:
            flash('ERROR! Recipe was not added.', 'error')
    if request.method == 'DELETE':
        print('del')
    return render_template('main/newOrd.html',
                           title='newOrd', form=form,
                           listOrdres=Ord.query.all())


# a Revoir
@main.route('/listAction')
def listAction():
    res = Act.query.all()
    list_actions = [r.as_dict() for r in res]
    return jsonify(list_actions)
