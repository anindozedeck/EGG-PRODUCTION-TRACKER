# Egg Production Tracker

A lightweight dashboard for recording egg collections by date and poultry shed,
and viewing recorded production totals.

## Live demo

https://egg-production-tracker-1.onrender.com

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

## Try it

Open the [live demo](https://egg-production-tracker-1.onrender.com) in your browser.

## Run

Start the app locally:

```powershell
py Day18_exercise.py
```

Then open http://127.0.0.1:5000.

## Who could use it in Kenya?

- **Small layer farms and family-run poultry businesses** that currently count
  eggs on paper or in a notebook. **Suggested price:** KES 300–500 per
  farm/month.
- **Multi-shed farms** that want to compare daily collections across sheds.
  **Suggested price:** KES 700–1,200 per farm/month.
- **Youth- and women-led poultry enterprises** that need a simple production
  record to support day-to-day planning. **Suggested starting point:** a free
  pilot, then KES 300–500 per farm/month for the basic plan.
- **Small egg cooperatives or collection points** could use an adapted version
  to record collections from member farms. The current tool records by shed,
  not by supplier, so member-level tracking would need to be added; pricing
  would depend on that adaptation.

It is most useful where the main need is consistent production records. It does
not currently manage feed, flock health, sales, expenses, or inventory.

## Suggested price point

These are **starting price hypotheses in Kenyan shillings (KES)**, not market
survey results. Offer a short, free pilot and test willingness to pay with local
poultry farmers before setting final prices. Keep the entry plan affordable and
charge more only when the service includes dependable hosting, persistent
records, backups, and support.

## Current prototype limitations

The current Flask prototype stores records in memory, so records are lost when
the server restarts. It has no user accounts, backups, or hosted subscription
features. Add persistent storage and secure deployment before using it for
business-critical records or charging customers for a hosted service.
