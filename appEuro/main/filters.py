from . import main


@main.app_template_filter()
def filters_date(dttm):
    return dttm.strftime('%d/%m/%Y')
