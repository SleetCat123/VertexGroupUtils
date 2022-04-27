import bpy
import bmesh

bl_info = {
    "name" : "VertexGroupUtils",
    "author" : "@sleetcat123(Twitter)",
    "version" : (1,0,0),
    "blender" : (2, 80, 0),
    "location": "SideMenu -> Item -> VertexGroupUtils",
    "description" : "",
    "category" : "Mesh"
}

### Funcs ###

### Panel ###
class UI_PT_VertexGroupUtil_Panel(bpy.types.Panel):
  bl_space_type = 'VIEW_3D'
  bl_region_type = 'UI'
  bl_category = "Item"
  bl_label = "VertexGroupUtil"

  def draw(self, context):
    layout = self.layout
    layout.separator()
    try:
        normalize_all = layout.operator('object.vertex_group_normalize_all', text="Normalize All Groups")
        normalize_all.group_select_mode='ALL'
        normalize_all.lock_active=False
        
        normalize_deform= layout.operator('object.vertex_group_normalize_all', text="Normalize Deform Groups")
        normalize_deform.group_select_mode='BONE_DEFORM'
        normalize_deform.lock_active=False
    except Exception:
        pass
    layout.separator()
    
    clean_active=layout.operator('object.vertex_group_clean', text="Clean Active Group")
    clean_active.group_select_mode='ACTIVE'
    clean_active.limit=0
    
    clean_activeB=layout.operator('object.vertex_group_clean', text="Clean Active Group 0.005")
    clean_activeB.group_select_mode='ACTIVE'
    clean_activeB.limit=0.005
    
    try:
        clean_deform=layout.operator('object.vertex_group_clean', text="Clean Deform Groups")
        clean_deform.group_select_mode='BONE_DEFORM'
        clean_deform.limit=0
        
        clean_deformB=layout.operator('object.vertex_group_clean', text="Clean Deform Groups 0.005")
        clean_deformB.group_select_mode='BONE_DEFORM'
        clean_deformB.limit=0.005
    except Exception:
        pass
    
    clean_all=layout.operator('object.vertex_group_clean', text="Clean All Groups")
    clean_all.group_select_mode='ALL'
    clean_all.limit=0
    
    clean_allB=layout.operator('object.vertex_group_clean', text="Clean All Groups 0.005")
    clean_allB.group_select_mode='ALL'
    clean_allB.limit=0.005


### Init ###
classes = [
  UI_PT_VertexGroupUtil_Panel,
]
def register():
  for c in classes:
    bpy.utils.register_class(c)

def unregister():
  for c in classes:
    bpy.utils.unregister_class(c)

if __name__ == "__main__":
  register()