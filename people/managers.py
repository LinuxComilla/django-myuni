from django.db import models
from django.db import connection, models
from django.core.exceptions import ObjectDoesNotExist

class PersonManager(models.Manager):
	"""Custom manager for the Person model"""
	def order_by_role(self):
		"""This one executes one big DB query, then another
			for each person returned. Not nice for my little DB server!
			(but no complicated comparisons to perform"""
		reln = self.model._meta.get_field('roles')
		join_table = connection.ops.quote_name(reln.m2m_db_table())
		person_id = connection.ops.quote_name(reln.m2m_column_name())
		role_id = connection.ops.quote_name(reln.m2m_reverse_name())
		""" This query bloody works!!!!! But I don't know how to return the result :("""
		query = """
		SELECT (MAX(weight)) AS `max_weight`, `auth_user`.`id`, `auth_user`.`username`, `auth_user`.`first_name`, `auth_user`.`last_name`, `auth_user`.`email`, `auth_user`.`password`, `auth_user`.`is_staff`, `auth_user`.`is_active`, `auth_user`.`is_superuser`, `auth_user`.`last_login`, `auth_user`.`date_joined`, `people_person`.`user_ptr_id`, `people_person`.`title_id`, `people_person`.`initial`, `people_person`.`course_taken_id`, `people_person`.`sid`, `people_person`.`heaviest_role_weight` FROM `people_person` INNER JOIN `auth_user` ON (`people_person`.`user_ptr_id` = `auth_user`.`id`) , `people_role` , `people_person_roles` WHERE people_person.user_ptr_id=people_person_roles.person_id AND people_role.object_ptr_id=people_person_roles.role_id GROUP BY `auth_user`.`id`, `auth_user`.`username`, `auth_user`.`first_name`, `auth_user`.`last_name`, `auth_user`.`email`, `auth_user`.`password`, `auth_user`.`is_staff`, `auth_user`.`is_active`, `auth_user`.`is_superuser`, `auth_user`.`last_login`, `auth_user`.`date_joined`, `people_person`.`user_ptr_id`, `people_person`.`title_id`, `people_person`.`initial`, `people_person`.`course_taken_id`, `people_person`.`sid`, `people_person`.`heaviest_role_weight` ORDER BY `max_weight` DESC
		"""
		cursor = connection.cursor()
		cursor.execute(query)
		people = []
		for row in cursor.fetchall():
			person = self.model.objects.get(pk=row[1])
			people.append(person)
		return people

	def by_role(self):
		"""Return a unique list of people, sorted by their heaviest role weight, in descending order
			...This one executes one big DB query, then constructs a list from the resulting
			queryset containing only the first of each person mentioned - resulting in a list
			which is ultimately sorted by heaviest role weight (heaviest comes first)"""
		return [x for x in self.order_by('roles') if x not in locals()['_[1]']]

class RoleManager(models.Manager):
	def heaviest(self):
		roles = self.all().order_by('-weight')
		return roles[0] if len(roles) else None
			
