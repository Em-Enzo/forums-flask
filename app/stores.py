
import datetime
import itertools
import copy



class BaseStore(object):
    """docstring for BaseStore"""
    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id
    
    def get_all(self):
        # get all items
        return self._data_provider

    def add(self, item_instance):
        # append item
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1


    def get_by_id(self, last_id):
        # get item by id 
        all_item_instances = self.get_all()
        result = None 
        for item_instance in all_item_instances:
          if item_instance.id == self._last_id :
              result = item_instance
              break  
        return result

    def entity_exists(self, item_instance):
        # check if item exists or not
        result = True
        if self.get_by_id(item_instance.id) is None:
          result = False
        return result

    def delete(self, id):
        # delete an item
        element = self.get_by_id(id)
        if element != None:
          self._data_provider.remove(element)
          print ("Item is deleted !")
        else:
          print ("Item not found !")
      

    def update(self, item_instance):
        # update the list or the DB
        all_item_instances = self.get_all()
        for index, element in enumerate(all_item_instances):
               if element.id == item_instance.id:
                    all_item_instances[index] = element
                    print ("updated ...!") 


class MemberStore(BaseStore):
    last_id = 1
    members =[] 

    def __init__(self):
          super(MemberStore, self).__init__(MemberStore.members, MemberStore.last_id)

    def get_by_name(self, name):
          # search and find the name in the list or the DB         
          all_members = self.get_all()
          #for element in all_members:
           #   if element.name == name:
            #      yield element 
          return (member for member in self.get_all() if member.name == name)

    def get_members_with_posts(self, all_posts):
      # returns all the members with thiere posts
      all_members =self.get_all()
      for member, post in itertools.product(all_members, all_posts):
        if member.id == post.member_id:
          member.posts.append(post)
      return all_members

    def get_top_two(self, all_posts):
      # returs the top two participation members
      all_members = list(self.get_members_with_posts(all_posts))
      all_members.sort(key= lambda element: len(element.posts), reverse= True) 
      return all_members[:10]



class PostStore(BaseStore):	 
    posts = []
    last_id = 1

    def __init__(self):
        super(PostStore, self).__init__(PostStore.posts, PostStore.last_id)

    def get_posts_by_date(self, datetime):
      all_posts = self.get_all()
      all_posts.sort(key= lambda x: x.date, reverse=True)
      return all_posts

    