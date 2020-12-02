import django_tables2 as tables


class LedgerTable(tables.Table):
    date = tables.DateTimeColumn(format ='d M Y')
    amount = tables.Column()
    category__category = tables.Column(verbose_name='Category')
    unit__title = tables.Column(verbose_name='Property')
    note = tables.Column()