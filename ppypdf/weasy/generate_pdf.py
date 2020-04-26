from weasyprint import HTML

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))

# html_file = "PDF_output_template.html"
# html_file = "sample.html"
html_file = "transcript_pdf_template.html"
full_transcript = {"sentences": [{'sentence': "my parents house if there's a big family gathered.",
                    'name': 'spk_0'}]}
template = env.get_template(html_file)


# template_vars = {"title": "Sales Funnel Report - National",
#                  "content": 'just trying'}
css_file = "style.css"
# css_file = "style2.css"
html_out = template.render(full_transcript)
HTML(string=html_out).write_pdf("report.pdf",
                                stylesheets=[css_file])
