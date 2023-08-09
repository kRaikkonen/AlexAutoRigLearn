import maya.cmds as base
import importlib
import Create_Locators

importlib.reload(Create_Locators)


def CreateJointWindows():
    
    global setPrefix
    setPrefix = "test"
    
    base.window("Joint Creation Window")
    base.rowColumnLayout(nc=1)
    base.button(l="Create Joints", w=200, c="Create_Joints.createJoints(Create_Locators.ReturnSpineAmount(), Create_Locators.ReturnFingersAmount())")
    base.button(l="Delete Joints", w=200, c="Create_Joints.deleteJoints()")
    base.showWindow()


def createJoints(spineAmount,amount):
    
    base.select(deselect=True)
    
    if base.objExists('RIG'):
        print('RIG Exists')
    else:
        jointGRP = base.group(em=True, name='RIG')

        ## Create Spine

        root = base.ls("Loc_ROOT")

        allSpines = base.ls("Loc_SPINE_*", type='locator')
        spine = base.listRelatives(*allSpines, p=True, f=True)
        
        rootPos = base.xform(root, q=True, t=True, ws=True)
        rootJoint = base.joint(radius=0.1, p=rootPos, name='RIG_TOOL')
        
        base.parent(rootJoint, w=True, a=True)
        base.parent(rootJoint, 'RIG', a=True)
        
        for i, s in enumerate(spine):
            pos = base.xform(s, q=True, t=True, ws=True)
            j = base.joint(radius=0.08, p=pos, name="RIG_SPINE_" + str(i))
            
        createArmJoints(spineAmount)    
            
            

def createArmJoints(amount):
    base.select(deselect = True)
    base.select("RIG_SPINE_"+str(amount - 1))
    L_Clavicle = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_Clavicle'), q = True, t = True, ws = True), name = "RIG_L_Clavicle")
    L_UpperArmJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_UpperArm'), q = True, t = True, ws = True), name = "RIG_L_UpperArm")
    L_ElbowJoint = base.joint(radius = 0.1, p = base.xform(base.ls("Loc_L_Elbow"), q = True, t = True, ws = True), name = "RIG_L_Elbow")
    if (base.objExists('Loc_L_ArmTwist_*')):
        L_armTwists = base.ls('Loc_L_ArmTwist_*', type = 'transform')
        print ("L_armTwists")
        for i, a in enumerate(L_armTwists):
            L_twistJoint = base.joint(radius = 0.1, p = base.xform(a, q = True, t = True, ws = True), name = "RIG_L_ArmTwist_"+str(i))
    else:
        print ('')
    L_WristJoint = base.joint(radius = 0.1, p = base.xform(base.ls("Loc_L_Wrist"), q = True, t = True, ws = True), name = "RIG_L_Wrist")
    
    base.select(deselect = True)
    base.select("RIG_SPINE_"+str(amount - 1))
    
    R_Clavicle = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_Clavicle'), q = True, t = True, ws = True), name = "RIG_R_Clavicle")
    R_UpperArmJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_UpperArm'), q = True, t = True, ws = True), name = "RIG_R_UpperArm")
    R_ElbowJoint = base.joint(radius = 0.1, p = base.xform(base.ls("Loc_R_Elbow"), q = True, t = True, ws = True), name = "RIG_R_Elbow")
    if (base.objExists('Loc_R_ArmTwist_*')):
        R_armTwists = base.ls('Loc_R_ArmTwist_*', type = 'transform')
        for j, at in enumerate(R_armTwists):
            R_twistJoint = base.joint(radius = 0.1, p = base.xform(at, q = True, t = True, ws = True), name = "RIG_R_ArmTwist_"+str(j))
    else:
        print ('')
    R_WristJoint = base.joint(radius = 0.1, p = base.xform(base.ls("Loc_R_Wrist"), q = True, t = True, ws = True), name = "RIG_R_Wrist")

            
def deleteJoints():
    base.select(deselect = True)
    base.delete(base.ls('RIG'))   


