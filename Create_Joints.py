import maya.cmds as base
import importlib
import CreateIKH
import Create_Locators




CreateIKH = importlib.reload(CreateIKH)
Create_Locators = importlib.reload(Create_Locators)


def CreateJointWindows():
    
    global setPrefix
    setPrefix = "test"
    
    base.window("Joint Creation Window")
    base.rowColumnLayout(nc=1)
    base.button(l="Create Joints", w=200, c="Create_Joints.createJoints(Create_Locators.ReturnSpineAmount(), Create_Locators.ReturnFingersAmount())")
    base.button(l="Delete Joints", w=200, c="Create_Joints.deleteJoints()")
    base.button(l = "Set Orientation", w = 200, c = "Create_Joints.setJointOrientation()")
    
    base.button(l = "Create IK", w = 200, c = "CreateIKH.IKHandles()")
    
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
        rootJoint = base.joint(radius=0.1, p=rootPos, name='RIG_ROOT')
        
        base.parent(rootJoint, w=True, a=True)
        base.parent(rootJoint, 'RIG', a=True)
        
        for i, s in enumerate(spine):
            pos = base.xform(s, q=True, t=True, ws=True)
            j = base.joint(radius=0.08, p=pos, name="RIG_SPINE_" + str(i))
            
        createArmJoints(spineAmount)
        createLegs()
        createHead(spineAmount)
        createFingerJoints(amount)
        print (amount)    
            
            

def createArmJoints(amount):
    base.select(deselect = True)
    base.select("RIG_SPINE_"+str(amount - 1))
    L_Clavicle = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_Clavicle'), q = True, t = True, ws = True), name = "RIG_L_Clavicle")
    L_UpperArmJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_UpperArm'), q = True, t = True, ws = True), name = "RIG_L_UpperArm")
    L_ElbowJoint = base.joint(radius = 0.1, p = base.xform(base.ls("Loc_L_Elbow"), q = True, t = True, ws = True), name = "RIG_L_Elbow")
   
   
    ## L Arm Twist
    
    if (base.objExists('Loc_L_ArmTwist_*')):
        L_armTwists = base.ls('Loc_L_ArmTwist_*', type = 'transform')
        print ("L_armTwists")
        for i, a in enumerate(L_armTwists):
            L_twistJoint = base.joint(radius = 0.1, p = base.xform(a, q = True, t = True, ws = True), name = "RIG_L_ArmTwist_"+str(i))
    else:
        print ('Starting Create L side arm twist')
    L_WristJoint = base.joint(radius = 0.1, p = base.xform(base.ls("Loc_L_Wrist"), q = True, t = True, ws = True), name = "RIG_L_Wrist")
    
    base.select(deselect = True)
    base.select("RIG_SPINE_"+str(amount - 1))
    
    R_Clavicle = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_Clavicle'), q = True, t = True, ws = True), name = "RIG_R_Clavicle")
    R_UpperArmJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_UpperArm'), q = True, t = True, ws = True), name = "RIG_R_UpperArm")
    R_ElbowJoint = base.joint(radius = 0.1, p = base.xform(base.ls("Loc_R_Elbow"), q = True, t = True, ws = True), name = "RIG_R_Elbow")
    
    
    ## R Arm Twist
    
    if (base.objExists('Loc_R_ArmTwist_*')):
        R_armTwists = base.ls('Loc_R_ArmTwist_*', type = 'transform')
        for j, at in enumerate(R_armTwists):
            R_twistJoint = base.joint(radius = 0.1, p = base.xform(at, q = True, t = True, ws = True), name = "RIG_R_ArmTwist_"+str(j))
    else:
        print ('Starting Create R side arm twist')
    R_WristJoint = base.joint(radius = 0.1, p = base.xform(base.ls("Loc_R_Wrist"), q = True, t = True, ws = True), name = "RIG_R_Wrist")


def createLegs():
    
    ## L side
    
    base.select(deselect = True)
    base.select('RIG_ROOT')
    
    L_upperLegJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_UpperLeg', type = 'transform'), q = True, t = True, ws = True), name = "RIG_L_UpperLeg")
    L_KneeJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_Knee'), q = True, t = True, ws = True), name = 'RIG_L_Knee')   
    L_FootJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_Foot') , q = True, t = True, ws = True), name = 'RIG_L_Foot') 
    L_ToeJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_Toes'), q = True, t = True, ws = True), name = 'RIG_L_Toes')
    
    ## R side
    
    base.select(deselect = True)
    base.select('RIG_ROOT')
    R_upperLegJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_UpperLeg', type = 'transform'), q = True, t = True, ws = True), name = "RIG_R_UpperLeg")
    R_KneeJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_Knee'), q = True, t = True, ws = True), name = 'RIG_R_Knee')  
    R_FootJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_Foot'), q = True, t = True, ws = True)  , name = 'RIG_R_Foot') 
    R_ToeJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_Toes'), q = True, t = True, ws = True), name = 'RIG_R_Toes')


def createIneverseFootRoll():
    base.select(deselect = True)
    L_heel = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_INV_Heel', type = 'transform'), q = True, t = True, ws = True), name = 'RIG_L_INV_Heel')
    L_toel = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_INV_Toes', type = 'transform'), q = True, t = True, ws = True), name = 'RIG_L_INV_Toes')
    L_ball = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_INV_Ball', type = 'transform'), q = True, t = True, ws = True), name = 'RIG_L_INV_Ball')
    L_ankle = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_L_INV_Ankle', type = 'transform'), q = True, t = True, ws = True), name = 'RIG_L_INV_Ankle')
    base.parent(L_heel, 'RIG')
    base.select(deselect = True)
    R_heel = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_INV_Heel', type = 'transform'), q = True, t = True, ws = True), name = 'RIG_R_INV_Heel')
    R_toel = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_INV_Toes', type = 'transform'), q = True, t = True, ws = True), name = 'RIG_R_INV_Toes')
    R_ball = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_INV_Ball', type = 'transform'), q = True, t = True, ws = True), name = 'RIG_R_INV_Ball')
    R_ankle = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_R_INV_Ankle', type = 'transform'), q = True, t = True, ws = True), name = 'RIG_R_INV_Ankle')
    base.parent(R_heel, 'RIG')

    
def createHead(amount):
    base.select(deselect = True)
    base.select("RIG_SPINE_"+str(amount - 1))   
    
    neckJoint = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_Neck_Start'), q = True, t = True, ws = True), name = "RIG_Neck_Start")
    base.joint(radius = 0.1, p = base.xform(base.ls('Loc_Neck_End'), q = True, t = True, ws = True), name = "RIG_Neck_End")
    base.joint(radius = 0.1, p = base.xform(base.ls('Loc_Head'), q = True, t = True, ws = True), name = "RIG_Head")
    
    base.select(deselect = True)
    base.select("RIG_Neck_End")
    
    jawJointStart = base.joint(radius= 0.1, p = base.xform(base.ls('Loc_Jaw_Start'), q = True, t = True, ws = True), name = 'RIG_Jaw_Start')
    jawJointEnd = base.joint(radius = 0.1, p = base.xform(base.ls('Loc_Jaw_End'), q = True, t = True, ws = True), name = 'RIG_Jaw_End')


def createFingerJoints(amount):
    for x in range(0, amount):
        createFinger(x)


def createFinger(i):
    base.select(deselect = True)
    base.select("RIG_L_Wrist")
    allFingers = base.ls( "Loc_L_Finger_" + str(i) + "_*", type='transform')
    fingers = base.listRelatives(allFingers, p = True, s = False)

        


    for x, f in enumerate(allFingers):

        pos = base.xform(f, q = True, t = True, ws = True)
        j = base.joint(radius = 0.1, p = pos, name = "RIG_L_Finger_"+str(i)+"_"+str(x))
        
        
    base.select(deselect = True)
    base.select("RIG_R_Wrist")
    r_allFingers = base.ls( "Loc_R_Finger_" + str(i) + "_*", type='transform')
    r_fingers = base.listRelatives(r_allFingers, p = True, s = False)
    print ('fingers')    
    
    for y, g in enumerate(r_allFingers):
        
        r_pos = base.xform(g, q = True, t = True, ws = True)
        r_j = base.joint(radius = 0.1, p = r_pos, name = "RIG_L_Finger_"+str(i)+"_"+str(y))    
        



def setJointOrientation():
    base.select('RIG_ROOT')
    base.joint(e = True, ch = True, oj = 'xyz')    

            
def deleteJoints():
    base.select(deselect = True)
    base.delete(base.ls('RIG'))   


