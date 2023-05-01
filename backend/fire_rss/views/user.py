from flask.views import MethodView
from flask_smorest import Blueprint

from ..base.restful import api_resp, resp_schema
from ..managers.user import UserManager
from ..schemas import user as user_schema

BPT = Blueprint("v1/user", __name__, description="User apis")


@BPT.route("/")
class Pets(MethodView):
    @BPT.arguments(user_schema.SearchUserSchema, location="query")
    @BPT.response(200, resp_schema(user_schema.UserSchema(many=True)))
    def get(self, args):
        """User list"""
        users = UserManager().get_user_list(args["page_size"], args["page_num"])
        return api_resp(UserManager.format_users(users))

    @BPT.arguments(user_schema.UserSchema)
    @BPT.response(200, resp_schema(user_schema.UserSchema))
    def post(self, data):
        """Add a new user"""
        user = UserManager().create_user(data["name"], data["password"])
        return api_resp(UserManager.format_user(user))
