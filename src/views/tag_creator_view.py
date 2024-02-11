from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_reponse import HttpResponse

class TagCreatorView:
    '''
        Resposabilidade de intagir com http
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]
        
        # logica de negocio
        
        # retorno do response
        return HttpResponse(status_code=200, body={"msg":"sucess"})

