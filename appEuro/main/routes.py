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


@main.route('/')
@main.route('/index')
def index():
#    return "Hello, World!"
    form = MyForm()
    print(url_for('.index'))
    return render_template('main/index.html',
                           form=form,
                           listActions=Act.query.all()
                           )


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
                           listActions=Act.query.all())


# with ajax et newAct
@main.route("/delRow", methods=["POST"])
def delRow():
    i = request.form.get("id", type=int)
    t = request.form.get("table", type=str)  # table
#    act = Act.query.filter_by(idAct=i).first()
    if t == 'newAct':
        item = Act.query.get(i)  # get idAct
        n = request.form.get("name", type=str)  # à effacer
        db.session.delete(item)
        db.session.commit()
        flash('Congratulations, stock {} deleted!'.format(
                item.name), 'success')
        return jsonify(ida=i, name=item.name)
    if t == 'newOrd':
        item = Ord.query.get(i)  # get idAct
        db.session.delete(item)
        db.session.commit()
        flash('Congratulations, order {} deleted!'.format(
                item.idAct), 'success')
        return jsonify(ido=i, sens=item.sens)


# with ajax et newAct
@main.route("/editRow", methods=["POST"])
def editRow():
    i = request.form.get("id", type=int)
    n = request.form.get("name", 0)
    s = request.form.get("symbol", type=str)
    t = request.form.get("table", type=str)  # table
#    act = Act.query.filter_by(name=n, symbol=s).first()_or_404()
    item = Act.query.get(i)  # get idAct
    if item is None:
        if t == 'newAct':
            # new act
            act = Act(name=item.name, symbol=item.symbol)
            db.session.add(act)
            # db.session.flush()
            print('Return new id Act value %s\n' % act.idAct)
            flash('New stock {}, added!'.format(
                act.name), 'success')
    else:
#        item.name = n
#        item.symbol = s
        flash('New stock {}, updated!'.format(
            item.name), 'success')
    print('item value: %s' % item)
    db.session.commit()
    if item is None:
        i = act.idAct
    return jsonify(idAct=i, table=t, nameEdit=item.name, symbol=item.symbol)


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
    elif request.method == 'POST':
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
            print('date: %s' % form.ordDate.data)
            print('quantity: %d' % form.quantity.data)
            print('idAct: %d' % form.idAct.data)
            ord = Ord(
                    sens=form.sens.data,
                    ordDate=form.ordDate.data,
                    PriceAchat=form.PriceAchat.data,
                    quantity=form.quantity.data,
                    idAct=form.idAct.data
                    )
            db.session.add(ord)
            db.session.commit()
            print(ord)
            flash('New order, {}, added!'.format(
                    ord.idAct), 'success')
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
