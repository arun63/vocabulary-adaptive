from wikitrivia.article import Article

import click
import json

# For now, hard-code the titles of articles you want to scrape here
SAMPLE_ARTICLES = (
    'Stephen Hawking',
    'Michael D. Higgins',
    'Trinity College Dublin',
    'Cristiano Ronaldo'
)

@click.command()
@click.argument('titles', nargs=-1)
@click.option('--output', type=click.File('w'), help='Output to JSON file')
def generate_trivia(titles, output):
    if len(titles) == 0:
        titles = SAMPLE_ARTICLES

    questions = []
    for article in titles:
        #click.echo('Analyzing \'{0}\''.format(article))
        article = Article(title=article)
        questions = questions + article.generate_trivia_sentences()

    if output:
        output_file = output.open()
        json.dump(questions, output_file, sort_keys=True, indent=4)
        click.echo('Output stored in {0}'.format(output.name))
    else:
      click.echo(json.dumps(questions, sort_keys=True, indent=4))

if __name__ == '__main__':
    generate_trivia()
