import io
from django.http import FileResponse
from django.views.generic import View

from reportlab.pdfgen import canvas


# ################

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse

from weasyprint import HTML


class IndexView(View):

    def get(self, request, *args, **kwargs):

        # Cria um arq para receber os dados e gerar o PDF
        buffer = io.BytesIO()

        # Cria o arq PDF
        pdf = canvas.Canvas(buffer)

        # Insere 'coisas' no PDF
        pdf.drawString(100, 100, 'Geek University')

        # Quando acabamos inserir coisas no PDF
        pdf.showPage()
        pdf.save()

        # Por fim, retornamos o buffer para o inicio do arq
        buffer.seek(0)

        # Faz o download do arq em PDF gerda
        # return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')

        # Abre o PDF direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')


class Index2View(View):

    def get(self, request, *args, **kwargs):
        texto = ['Esse é um texto que será salvo em pdf', 'Obrigado!', 'Att,', 'Alguem da Silva']

        html_string = render_to_string('relatorio.html', {'texto': texto})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/relatorio2.pdf')

        fs = FileSystemStorage('/tmp/')

        with fs.open('relatorio2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            #Faz dowload do arq pdf
            # response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf'

            #Abre o pdf no navegador
            response['Content-Disposition'] = 'inline filename="relatorio2.pdf'

        return response
