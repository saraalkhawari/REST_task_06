from rest_framework.permissions import BasePermission
from datetime import date

class IsOwnerStaff(BasePermission):
	message  ='Only Owners and Staff have Access !'

	def has_object_permission(self,request,view,obj):
		if request.user.is_staff or request.user == obj.user :
			return True 
		return False


class UpcommingBookingsOnly(BasePermission):
	message = "Date is in the Past"

	def has_object_permission(self,request,view,obj):
		days_left = (obj.date - date.today()).days
		if days_left > 3 :
			return True
		return False