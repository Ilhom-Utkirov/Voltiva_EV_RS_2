from flask import Blueprint, jsonify, request
from authentification import check_credentials
import requests
import pandas as pd

zeroshot_bp = Blueprint('zeroshot_bp', __name__)

@zeroshot_bp.before_request
def before_request():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not check_credentials(auth_header):
        return jsonify({"message": "Unauthorized"}), 401

@zeroshot_bp.route('/zeroshot/get_all_categories', methods=['GET'])
def zeroshot_get_all_categories():
    return jsonify({"message": "Zeroshot get_all_categories"}), 200


@zeroshot_bp.route('/zeroshot/action2', methods=['POST'])
def zeroshot_action2():
    data = request.get_json()
    input_categories = data.get('categories', [])

    # Replace this URL with the actual API endpoint your colleague provided
    api_url = "https://example.com/api/categories"  # Update with the correct URL

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        api_data = response.json()

        # Extract categories and subcategories from API response
        categories = []
        for category in api_data['data']:
            categories.append({
                'name': category['name'],
                'children': [child['name'] for child in category['children']]
            })

        # Create a DataFrame
        df_categories = pd.DataFrame(categories)

        # Check if input categories exist in the DataFrame
        results = []
        for category in input_categories:
            if category in df_categories['name'].values:
                results.append({
                    'category': category,
                    'exists': True,
                    'subcategories': df_categories[df_categories['name'] == category]['children'].values[0]
                })
            else:
                results.append({'category': category, 'exists': False})

    except requests.exceptions.RequestException as e:
        return jsonify({"message": "Failed to fetch categories", "error": str(e)}), 500

    return jsonify({"message": "Zeroshot Action 2", "data": data, "results": results}), 200

# @zeroshot_bp.route('/zeroshot/action2', methods=['POST'])
# def zeroshot_action2():
#     data = request.get_json()
#     return jsonify({"message": "Zeroshot Action 2", "data": data}), 200
