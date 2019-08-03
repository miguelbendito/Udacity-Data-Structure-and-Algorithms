class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.visited = False

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True

    for g in group.get_groups():
        if group.visited == False:
            group.visited = True
            r = is_user_in_group(user, g)
            if r:
                return True

    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)



child.add_group(sub_child)
parent.add_group(child)

checker = is_user_in_group(sub_child_user, parent)
print (checker)

case_2 = is_user_in_group("sub", parent)
# user not found case
print(case_2)

grandpa = Group("grandpa")
grandma = Group("grandma")
grandpa.add_group(grandma)
grandma.add_group(grandpa)
case_3 = is_user_in_group("hi", grandpa)
# only the group parent is present

print(case_3)
