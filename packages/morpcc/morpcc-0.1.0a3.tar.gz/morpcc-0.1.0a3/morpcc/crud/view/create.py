import morepath
import html
import deform
from morpfw.crud import permission as crudperms
from ..model import CollectionUI, ModelUI
from ...app import App
from ...util import dataclass_to_colander


@App.html(model=CollectionUI, name='create', template='master/simple-form.pt',
          permission=crudperms.Create)
def create(context, request):
    formschema = dataclass_to_colander(
        context.collection.schema, include_fields=context.create_include_fields,
        exclude_fields=context.create_exclude_fields)
    return {
        'page_title': 'Create %s' % html.escape(
            str(context.collection.__class__.__name__.replace('Collection', ''))),
        'form_title': 'Create',
        'form': deform.Form(formschema(), buttons=('Submit',)),
    }


@App.html(model=CollectionUI, name='create', template='master/simple-form.pt',
          permission=crudperms.Create, request_method='POST')
def process_create(context, request):
    formschema = dataclass_to_colander(
        context.collection.schema, include_fields=context.create_include_fields,
        exclude_fields=context.create_exclude_fields)

    controls = list(request.POST.items())
    form = deform.Form(formschema(), buttons=('Submit', ))

    failed = False
    try:
        data = form.validate(controls)
    except deform.ValidationFailure as e:
        form = e
        failed = True

    if not failed:
        obj = context.collection.create(data)
        obj.save()
        return morepath.redirect(request.link(context.modelui_class(request, obj, context)))

    return {
        'page_title': 'Create %s' % html.escape(
            str(context.collection.__class__.__name__.replace('Collection', ''))),
        'form_title': 'Create',
        'form': form,
    }
