#!/usr/bin/python3

"""Flask Generic API"""

from flask import Flask, request, jsonify, abort

APP = Flask(__name__)

@APP.route("/", methods=['GET','POST'])
def root():
    """
    ROOT
    """
    return_data = dict()
    try:
        print(request.get_json())
        return_data["success"] = True
    except Exception as e:
        print(e.message)
        return_data["success"] = False
    except:
        abort(500)
    return jsonify(return_data)

def main():
    """
    Main function
    """
    APP.run(threaded=True, host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()

