# App - Eureka Backend

Struggling to find ideas for your next app? Eureka is here to help! This application aggregates and filters a variety of project ideas by scraping data from hackerearth, tailored to your specific needs.

Developed during the Hackofiesta hackathon, this project's frontend can be accessed [here](https://github.com/tanishabisht/App-Eureka).


## Instructions to run the application
To set up and run the backend of the application, follow these simple steps:

1. **Install Python**: Ensure Python is installed on your machine.
2. **Run the Application**: Navigate to the application's directory in the command line and execute:
   ```bash
   python3 app.py
   ```


## Devfolio Scraper

The Devfolio Scraper component automatically extracts project ideas and related data, organizing it into a structured JSON format stored in the `Database` folder. Sample structure of the scraped data:
```json
{
    "allData": [
        {
            "idNo": "unique index number",
            "name": "project name",
            "desc": "short project description",
            "devfolioLink": "https://devfolio.co/submissions/project-link",
            "githubLinks": ["link1", "link2"],
            "special_mention": "award or position achieved",
            "stacksUsed": ["Technology1", "Technology2", "Technology3"],
            "longDesc": "detailed project description"
        }
    ]
}
```


## Team
`Tanisha` [`Adithya Balachandra`](https://github.com/Addii45) [`Arjun Gopikrishnan`](https://github.com/arjun-gopikrishnan) [`Aditi Rastogi`](https://github.com/AditiRastogi250701) [`Prakhar Singh`](https://github.com/PrSi007)


## Technologies used
`python` `selenium` `flask`