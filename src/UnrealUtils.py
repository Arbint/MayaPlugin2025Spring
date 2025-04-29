import os
import unreal

def CreateBaseImportTask(importPath):
    importTask = unreal.AssetImportTask()
    importTask.filename = importPath

    fileName = os.path.basename(importPath).split('.')[0]
    importTask.destination_path = '/Game/'  + fileName

    importTask.automated = True
    importTask.save = True
    importTask.replace_existing = True

    return importTask


def ImportSkeletalMesh(meshPath):
    importTask = CreateBaseImportTask(meshPath)

    importOption = unreal.FbxImportUI()
    importOption.import_mesh = True
    importOption.import_as_skeletal = True
    importOption.skeletal_mesh_import_data.set_editor_property('import_morph_targets', True)
    importOption.skeletal_mesh_import_data.set_editor_property('use_t0_as_ref_pose', True)

    importTask.options = importOption

    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([importTask])
    return importTask.get_objects()[-1]

def ImportMeshAndAnimations(meshPath, animDir):
    mesh = ImportSkeletalMesh(meshPath) 
    print(mesh)

ImportMeshAndAnimations("D:/MayaToUETemp/Alex.fbx", "D:/MayaToUETemp/animations/")
