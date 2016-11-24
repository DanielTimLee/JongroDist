from flask_restful import fields

user_field = {
    'username': fields.String(attribute='username'),
    'nickname': fields.String(attribute='nickname'),
    'name': fields.String(attribute='name'),
    'gender': fields.String(attribute='gender'),
    'company': fields.String(attribute='company'),
    'type': fields.String(attribute='type'),
    'email': fields.String(attribute='email'),
    'join': fields.String(attribute='created_date')
}

document_field = {
    "id": fields.Integer(attribute='id'),
    "title": fields.String(attribute='title'),
    "content": fields.String(attribute="content"),
    'board_name': fields.String(attribute='board_name'),
    'board_title': fields.String(attribute='board_title'),
    "read_count": fields.Integer(attribute="read_count"),
    "like_count": fields.Integer(attribute="like_count"),
    "user_id": fields.Integer(attribute="user_id"),
    "username": fields.String(attribute="username"),
    "created_date": fields.String(attribute="created_date")
}

document_list_fields = {
    'items': fields.Nested(document_field)
}

project_field = {
    "id": fields.Integer(attribute='id'),
    "title": fields.String(attribute='title'),
    "description": fields.String(attribute="description"),
    "target_count": fields.Integer(attribute="target_count"),
    "contact_type": fields.String(attribute="contact_type"),
    "valid_customer": fields.String(attribute="valid_customer"),
    "keyword_num": fields.String(attribute="keyword_num"),
    "status": fields.String(attribute="status"),
    # TODO : user_id는 나중에 모두 뺄 수 있도록
    "user_id": fields.Integer(attribute="user_id"),
    "username": fields.String(attribute="username"),
    "created_date": fields.String(attribute="created_date")
}

project_list_fields = {
    'items': fields.Nested(project_field)
}

project_target_field = {
    "project_id": fields.String(attribute='project_id'),
    "target_id": fields.String(attribute='target_id'),
    "user_name": fields.String(attribute="name"),
    "user_id": fields.String(attribute="user_id"),
    "user_nickname": fields.String(attribute="nickname"),
    "user_phone": fields.String(attribute="phone"),
    "user_email": fields.String(attribute="email"),
    "user_birthday": fields.String(attribute="birthday"),
    "user_gender": fields.String(attribute="gender"),
}

project_target_list_field = {
    'items': fields.Nested(project_target_field)
}

notification_field = {
    'id': fields.Integer(attribute='id'),
    'content': fields.String(attribute='content'),
    'extra_data': fields.String(attribute='extra_data'),
    'target_id': fields.String(attribute='target_id'),
    'status': fields.String(attribute='status'),
    'created_date': fields.String(attribute="created_date"),
}

notification_list_fields = {
    'items': fields.Nested(notification_field)
}

keyword_field = {
    'ranking': fields.String(attribute='ranking'),
    'keyword': fields.String(attribute='keyword'),
    'lookalike_score': fields.String(attribute='lookalike_score'),
    'found_target': fields.String(attribute='found_target'),
    'advertise_rage': fields.String(attribute='advertise_range')
}

demo_field = {
    'keyword': fields.String(attribute='keyword'),
    'keyword_data': fields.String(attribute='keyword_data'),
}

analyze_result_fields = {
    'project': fields.Nested(project_field),
    'keyword': fields.Nested(keyword_field),
    'demo': fields.Nested(demo_field)
}
