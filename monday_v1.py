###
### Monday API Functions
###

import requests
api_url = 'https://api.monday.com'

### Users ###

def get_all_users(secret, api_url, page_offset=0, results_per_page=25, result_offset=0, order_by_latest=False):
    data = {
            'api_key': secret,
            'page': page_offset,
            'per_page': results_per_page,
            'offset': result_offset,
            'order_by_latest': order_by_latest
           }
    endpoint = '/v1/users.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def get_user(secret, user_id):
    data = {
            'api_key': secret,
            'id': user_id
           }
    endpoint = f'/v1/users/{user_id}.json'
    r = requests.get(url=url+endpoint, data=data)
    return r

def get_specific_user_post(secret, api_url, user_id, page_offset=0, results_per_page=25, result_offset=0):
    data = {
            'api_key': secret,
            'page': page_offset,
            'per_page': results_per_page,
            'offset': result_offset
           }
    endpoint = f'/v1/users/{user_id}/posts.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def get_specific_user_newsfeed(secret, api_url, user_id, page_offset=0, results_per_page=25, result_offset=0):
    data = {
            'api_key': secret,
            'id': user_id,
            'page': page_offset,
            'per_page': results_per_page,
            'offset': result_offset,
           }
    endpoint = f'/v1/users/{user_id}/newsfeed.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

### Updates ###

def get_all_account_updates(secret, api_url, page_offset=0, results_per_page=25, result_offset=0, since_date='', until_date='', updated_since_date='', updated_until_date=''):
    data = {
            'api_key': secret,
            'page': page_offset,
            'per_page': results_per_page,
            'offset': result_offset,
            'since': since_date,
            'until': until_date,
            'updated_since': updated_since_date,
            'updated_until': updated_until_date,
           }
    endpoint = '/v1/updates.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def create_update(secret, api_url, user_id, pulse_id, update_text):
    data = {
            'api_key': secret,
            'user': user_id,
            'pulse': pulse_id,
            'update_text': update_text,
           }
    endpoint = '/v1/updates.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

def get_specific_post(secret, api_url, update_id):
    data = {
            'api_key': secret,
            'id': update_id,
           }
    endpoint = f'/v1/updates/{update_id}.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def delete_update(secret, api_url, update_id):
    data = {
            'api_key': secret,
            'id': update_id,
           }
    endpoint = f'/v1/updates/{update_id}.json'
    r = requests.delete(url=api_url+endpoint, data=data)
    return r.status_code

def like_update(secret, api_url, update_id, user_id):
    data = {
            'api_key': secret,
            'id': update_id,
            'user': user_id,
           }
    endpoint = f'/v1/updates/{update_id}/like.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

def unlike_update(secret, api_url, update_id, user_id):
    data = {
            'api_key': secret,
            'id': update_id,
            'user': user_id
           }
    endpoint = f'/v1/updates/{update_id}/unlike.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

### Pulses ###

def get_all_account_pulses(secret, api_url, page_offset=0, results_per_page=25, result_offset=0, order_by_latest=False, since_date='', until_date=''):
    data = {
            'api_key': secret,
            'page': page_offset,
            'per_page': results_per_page,
            'offset': result_offset,
            'order_by_latest': order_by_latest,
            'since': since_date,
            'until': until_date,
           }
    endpoint = '/v1/pulses.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def get_pulse_info(secret, api_url, pulse_id):
    data = {
            'api_key': secret,
            'id': pulse_id,
           }
    endpoint = f'/v1/pulses/{pulse_id}.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def update_pulse_attributes(secret, api_url, pulse_id, pulse_name):
    data = {
            'api_key': secret,
            'id': pulse_id,
            'name': pulse_name,
           }
    endpoint = f'/v1/pulses/{pulse_id}.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def delete_pulse(secret, api_url, pulse_id, archive_pulse=False):
    data = {
            'api_key': secret,
            'id': pulse_id,
            'archive': archive_pulse,
           }
    endpoint = f'/v1/pulses/{pulse_id}.json'
    r = requests.delete(url=api_url+endpoint, data=data)
    return r.status_code

def get_pulse_subscribers(secret, api_url, pulse_id, page_offset=0, results_per_page=25, result_offset=0)
    data = {
            'api_key': secret,
            'id': pulse_id,
            'page': page_offset,
            'per_page': results_per_page,
            'offset': result_offset,
           }
    endpoint = f'/v1/pulses/{pulse_id}/subscribers.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def add_pulse_subscriber(secret, api_url, pulse_id, user_id, as_admin=False):
    data = {
            'api_key': secret,
            'id': pulse_id,
            'user_id': user_id,
            'as_admin': as_admin,
           }
    endpoint = f'/v1/pulses/{pulse_id}/subscribers.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def delete_pulse_subscriber(secret, api_url, pulse_id, user_id):
    data = {
            'api_key': secret,
            'id': pulse_id,
            'user_id': user_id,
           }
    endpoint = '/v1/pulses/{pulse_id}/subscribers/{user_id}.json'
    r = requests.delete(url=api_url+endpoint, data=data)
    return r.status_code

def get_notes_from_pulse(secret, api_url, pulse_id):
    data = {
            'api_key': secret,
            'id': pulse_id,
           }
    endpoint = '/v1/pulses/{pulse_id}/notes.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def create_pulse_note(secret, api_url, pulse_id, note_title, note_content, user_id, owners_only=False, create_update_notification=False):
    data = {
            'api_key': secret,
            'id': pulse_id,
            'title': note_title,
            'content': note_content,
            'owners_only': owners_only,
            'user_id': user_id,
            'create_update': create_update_notification,
           }
    endpoint = '/v1/pulses/{pulse_id}/notes.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

def delete_pulse_note(secret, api_url, pulse_id, note_id):
    data = {
            'api_key': secret,
            'id': pulse_id,
            'note_id': note_id,
           }
    endpoint = '/v1/pulses/{pulse_id}/notes/{note_id}.json'
    r = requests.delete(url=api_url+endpoint, data=data)
    return r.status_code

def get_pulse_updates(secret, api_url, pulse_id, updates_page, results_per_page=25):
    data = {
            'api_key': secret,
            'id': pulse_id,
            'page': updates_page,
            'limit': results_per_page,
           }
    endpoint = '/v1/pulses/{pulse_id}/updates.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

### Boards ###

def get_all_boards(secret, api_url, results_per_page, only_globals=False, order_by_latest=False):
    data = {
            'api_key': secret,
            'per_page': results_per_page,
            'only_globals': only_globals,
            'order_by_latest': order_by_latest
           }
    endpoint = '/v1/boards.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def create_board(secret, api_url, user_id, board_name, board_description='', board_type=''):
    data = {
            'api_key': secret,
            'user_id': user_id,
            'name': board_name,
            'description': board_description,
            'board_kind': board_type
           }
    endpoint = '/v1/boards.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

def get_board_details(secret, api_url, board_id):
    data = {
            'api_key': secret,
            'board_id': board_id
           }
    endpoint = f'/v1/boards/{board_id}.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def archive_board(secret, api_url, board_id):
    data = {
            'api_key': secret,
            'board_id': board_id
           }
    endpoint = f'/v1/boards/{board_id}.json'
    r = requests.delete(url=api_url+endpoint, data=data)
    return r.status_code

def get_all_board_groups(secret, api_url, board_id, show_archived=False, show_deleted=False):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'show_archived': show_archived,
            'show_deleted': show_deleted
           }
    endpoint = f'/v1/boards/{board_id}/groups.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def update_group_info(secret, api_url, board_id, group_id, group_title, group_colour):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'group_id': group_id,
            'title': group_title,
            'color': group_colour
           }
    endpoint = f'/v1/boards/{board_id}/groups.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def create_group_in_board(secret, api_url, board_id, group_title):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'title': group_title
           }
    endpoint = f'/v1/boards/{board_id}/groups.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

def move_group_to board(secret, api_url, board_id, group_id, user_id, destination_board_id):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'group_id': group_id,
            'user_id': user_id,
            'dest_board_id': destination_board_id
           }
    endpoint = f'/v1/boards/{board_id}/groups/{group_id}/move.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

def archive_group(secret, api_url, board_id, group_id):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'group_id': group_id
           }
    endpoint = f'/v1/boards/{board_id}/groups/{group_id}.json'
    r = requests.delete(url=api_url+endpoint, data=data)
    return r.status_code

def get_all_board_columns(secret, api_url, board_id, all_columns=False):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'all_columns': all_columns
           }
    endpoint = f'/v1/boards/{board_id}/columns.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def add_new_column_to_board(secret, api_url, board_id, column_name, column_type, column_labels=''):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'title': column_name,
            'type': column_type,
            'labels': column_labels
           }
    endpoint = f'/v1/boards/{board_id}/columns.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

def update_column_definition(secret, api_url, board_id, column_id, column_title, column_colour, column_labels=''):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id,
            'title': column_title,
            'color': column_colour,
            'labels': column_labels
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def delete_column(secret, api_url, board_id, column_id):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}.json'
    r = requests.delete(url=api_url+endpoint, data=data)
    return r.status_code

def get_pulse_column_value(secret, api_url, board_id, column_id, pulse_id, return_as_array=False):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id,
            'pulse_id': pulse_id,
            'return_as_array': return_as_array
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}/value.json '
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def update_text_column(secret, api_url, board_id, column_id, pulse_id, text):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id,
            'pulse_id': pulse_id,
            'text': text
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}/text.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def update_person_column(secret, api_url, board_id, column_id, pulse_id, user_id):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id,
            'pulse_id': pulse_id,
            'user_id': user_id
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}/person.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def update_status_column(secret, api_url, board_id, column_id, pulse_id, colour_index, update_id):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id,
            'pulse_id': pulse_id,
            'color_index': colour_index,
            'update_id': update_id
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}/status.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def update_date_column(secret, api_url, board_id, column_id, pulse_id, date_string):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id,
            'pulse_id': pulse_id,
            'date_str': date_string
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}/date.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def update_numeric_column(secret, api_url, board_id, column_id, pulse_id, numeric_value):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id,
            'pulse_id': pulse_id,
            'value': numeric_value
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}/numeric.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def update_tag_column(secret, api_url, board_id, column_id, pulse_id, tags_string):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id,
            'pulse_id': pulse_id,
            'tags': tags_string
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}/tags.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def update_timeline_column(secret, api_url, board_id, column_id, pulse_id, from_date, to_date):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'column_id': column_id,
            'pulse_id': pulse_id,
            'from': from_date,
            'to': to_date
           }
    endpoint = f'/v1/boards/{board_id}/columns/{column_id}/timeline.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def get_board_pulses(secret, api_url, board_id, page_offset=0, results_per_page=25, order_by=''):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'page': page_offset,
            'per_page': results_per_page,
            'order_by': order_by
           }
    endpoint = f'/v1/boards/{board_id}/pulses.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def create_pulse(secret, api_url, board_id, user_id, pulse_name, pulse_hash='', pulse_photo_from_url='', pulse_update_hash='', pulse_update_text='', pulse_group_id='', add_to_bottom=False):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'user_id': user_id,
            'pulse[name]': pulse_name,
            'pulse': pulse_hash,
            'pulse[photo_from_url]': pulse_photo_from_url,
            'update': pulse_update_hash,
            'update[text]': pulse_update_text,
            'group_id': pulse_group_id,
            'add_to_bottom': add_to_bottom
           }
    endpoint = f'/v1/boards/{board_id}/pulses.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

def move_pulse(secret, api_url, board_id, user_id, group_id, pulse_ids, destination_board_id, force_move_to_board=False):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'user_id': user_id,
            'group_id': group_id,
            'pulse_ids': pulse_ids,
            'dest_board_id': destination_board_id,
            'force_move_to_board': force_move_to_board
           }
    endpoint = f'/v1/boards/{board_id}/pulses/move.json'
    r = requests.post(url=api_url+endpoint, data=data)
    return r.status_code

def get_board_subscribers(secret, api_url, board_id, page_offset, results_per_page, result_offset):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'page': page_offset,
            'per_page': results_per_page,
            'offset': result_offset
           }
    endpoint = f'/v1/boards/{board_id}/subscribers.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

def add_board_subscriber(secret, api_url, board_id, user_id, as_admin=False):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'user_id': user_id,
            'as_admin': as_admin
           }
    endpoint = f'/v1/boards/{board_id}/subscribers.json'
    r = requests.put(url=api_url+endpoint, data=data)
    return r.status_code

def delete_board_subscriber(secret, api_url, board_id, user_id):
    data = {
            'api_key': secret,
            'board_id': board_id,
            'user_id': user_id
           }
    endpoint = f'/v1/boards/{board_id}/subscribers/{user_id}.json'
    r = requests.delete(url=api_url+endpoint, data=data)
    return r.status_code

### Tags ###

def get_tag(secret, api_url, tag_id):
    data = {
            'api_key': secret,
            'id': tag_id
           }
    endpoint = f'/v1/tags/{tag_id}.json'
    r = requests.get(url=api_url+endpoint, data=data)
    return r

###
### Other useful functions
###

# Used to get the last created pulse id so that fields can be populated against it
def get_last_created_pulse_id(secret, api_url, board_id):
    data = {'api_key': secret,
            'board_id': board_id,
            'page': '0',
            'per_page': '1',
            'order_by': 'created_at_desc'
            }
    endpoint = f'/v1/boards/{board_id}/pulses.json'
    r = requests.get(url=url+endpoint, data=data)
    raw_json = r.json()
    last_pulse_id = raw_json[0]['pulse']['id']
    return last_pulse_id