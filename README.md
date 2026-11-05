# Egg Production Tracker

A lightweight dashboard for recording egg collections by date and poultry shed,
and viewing recorded production totals.

## Who could use it in Kenya?

- **Small layer farms and family-run poultry businesses** that currently count
  eggs on paper or in a notebook.
- **Multi-shed farms** that want to compare daily collections across sheds.
- **Youth- and women-led poultry enterprises** that need a simple production
  record to support day-to-day planning.
- **Small egg cooperatives or collection points** could use an adapted version
  to record collections from member farms. The current tool records by shed,
  not by supplier, so member-level tracking would need to be added.

It is most useful where the main need is consistent production records. It does
not currently manage feed, flock health, sales, expenses, or inventory.

## Suggested price point

These are **starting price hypotheses in Kenyan shillings (KES)**, not market
survey results:

| Offer | Suggested price | Intended customer |
| --- | ---: | --- |
| Local demo or pilot | Free | One farm evaluating the workflow |
| Basic hosted plan | KES 300–500 per farm/month | A small farm recording production |
| Multi-shed hosted plan | KES 700–1,200 per farm/month | A farm that needs shed-level records and support |

Start with a free, short pilot and test willingness to pay with local poultry
farmers before setting final prices. Keep the entry plan affordable and charge
more only when the service includes dependable hosting, persistent records,
backups, and support.

## Current prototype limitations

The current Flask prototype stores records in memory, so records are lost when
the server restarts. It has no user accounts, backups, or hosted subscription
features. Add persistent storage and secure deployment before using it for
business-critical records or charging customers for a hosted service.
