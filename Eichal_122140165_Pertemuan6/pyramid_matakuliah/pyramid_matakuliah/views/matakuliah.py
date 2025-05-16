from pyramid.view import view_config
from pyramid.response import Response
import json

@view_config(route_name='get_matkul', renderer='json', request_method='GET')
def get_matkul(request):
    id = request.matchdict.get('id')
    matkul = request.dbsession.query(Matakuliah).get(id)
    if not matkul:
        return Response(json_body={'error': 'Not found'}, status=404)
    return matkul.to_dict()

@view_config(route_name='list_matkul', renderer='json', request_method='GET')
def list_matkul(request):
    matkuls = request.dbsession.query(Matakuliah).all()
    return [m.to_dict() for m in matkuls]

@view_config(route_name='create_matkul', renderer='json', request_method='POST')
def create_matkul(request):
    data = request.json_body
    matkul = Matakuliah(**data)
    request.dbsession.add(matkul)
    return Response(json_body={'status': 'created'}, status=201)

@view_config(route_name='update_matkul', renderer='json', request_method='PUT')
def update_matkul(request):
    id = request.matchdict.get('id')
    matkul = request.dbsession.query(Matakuliah).get(id)
    if not matkul:
        return Response(json_body={'error': 'Not found'}, status=404)
    data = request.json_body
    for key, value in data.items():
        setattr(matkul, key, value)
    return {'status': 'updated'}

@view_config(route_name='delete_matkul', renderer='json', request_method='DELETE')
def delete_matkul(request):
    id = request.matchdict.get('id')
    matkul = request.dbsession.query(Matakuliah).get(id)
    if not matkul:
        return Response(json_body={'error': 'Not found'}, status=404)
    request.dbsession.delete(matkul)
    return {'status': 'deleted'}
