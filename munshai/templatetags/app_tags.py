from django import template
from munshai.models import Document, Client, DOC_TYPES
import collections
doc_info = collections.namedtuple('doc_info',['type','name','link'])
register = template.Library()


@register.filter
def get_doc_name(type, client_id):
    val = Document.objects.filter(client_id=client_id, document_type=type).first()
    return val.document_name if val else ""

@register.filter
def get_doc_info(client_id):
    doc_types = [doc_type[0] for doc_type in DOC_TYPES]
    to_return=[]
    for doc_type in doc_types:
        val = Document.objects.filter(client_id=client_id, document_type=doc_type).first()
        d = doc_info(type=doc_type,name=val.document_name if val else "",link=val.document_id if val else "")
        to_return.append(d)
    return to_return



@register.filter
def get_doc_types(ip):
    return [doc_type[0] for doc_type in DOC_TYPES]
