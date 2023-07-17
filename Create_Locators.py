import maya.cmds as base







def createField():
    base.text("Spine Joints Count", l="Spine Joints Count")
    spineJointsCount = base.intField(minValue=1, maxValue=10, value=4)

    base.text("Finger Amount",l = "Fingers Amount")
    fingerCount = base.intField(minValue = 1, maxValue = 10, value = 5)

##base.button(l="Edit Mode", w=200, c="lockAll(editMode)")    







def createLocators():
    if base.objExists("Loc_Master"):
        print('Loc_Master already exists')
    else:
        base.group(em=True, name="Loc_Master")

    root = base.spaceLocator(n='Loc_ROOT')
    base.scale(0.1, 0.1, 0.1, root)
    base.move(0, 1, 0, root)
    base.parent(root, "Loc_Master")
    createSpine()


def createSpine():
    for i in range(0, base.intField(spineJointsCount, query=True, value=True)):
        spine = base.spaceLocator(n='Loc_SPINE_' + str(i))
        base.scale(0.1, 0.1, 0.1, spine)
        if i == 0:
            base.parent(spine, 'Loc_ROOT')
        else:
            base.parent(spine, 'Loc_SPINE_' + str(i - 1))
        base.move(0, 1.25 + (0.25 * i), 0, spine)

    createArms(1)
    createArms(-1)
    createLegs(1)
    createLegs(-1)




    



def createArms(side):
    if side == 1:
        if base.objExists('L_Arm_GRP'):
            print('Left Arm already exists')
        else:
            L_arm = base.group(em=True, name='L_Arm_GRP')
            base.parent(L_arm, 'Loc_SPINE_' + str(base.intField(spineJointsCount, query=True, value=True) - 1))
            
            #Create L_UpperArm
            L_upperArm = base.spaceLocator( n = 'Loc_L_UpperArm')
            base.scale(0.1,0.1,0.1, L_upperArm)
            base.parent(L_upperArm, L_arm)
            
            #Create L_Elbow
            L_Elbow = base.spaceLocator( n = 'Loc_L_Elbow')
            base.scale(0.1,0.1,0.1, L_Elbow)
            base.parent(L_Elbow, L_upperArm)
            
            #Create L_Wrist
            L_Wrist = base.spaceLocator( n = 'Loc_L_Wrist')
            base.scale(0.1,0.1,0.1, L_Wrist)
            base.parent(L_Wrist, L_Elbow)
            
            
            
            base.move(0.35 * side, 1 + 0.25 * base.intField(spineJointsCount, query = True, value = True), 0, L_arm)
            base.move(0.6 * side, 1.4, -0.2, L_Elbow)
            base.move(0.8 * side, 1, 0, L_Wrist)
            
            
            createHands(side, L_Wrist)
            
                        
           
            
            

    else:
        if base.objExists('R_Arm_GRP'):
            print('Right Arm already exists')
        else:
            R_arm = base.group(em=True, name='R_Arm_GRP')
            base.parent(R_arm, 'Loc_SPINE_' + str(base.intField(spineJointsCount, query=True, value=True) - 1))
            
            
            #Create R_UpperArm
            R_upperArm = base.spaceLocator( n = 'Loc_R_UpperArm')
            base.scale(0.1,0.1,0.1, R_upperArm)
            base.parent(R_upperArm, R_arm)
            
            #Create R_Elbow
            R_Elbow = base.spaceLocator( n = 'Loc_R_Elbow')
            base.scale(0.1,0.1,0.1, R_Elbow)
            base.parent(R_Elbow, R_upperArm)
            
            #Create R_Wrist
            R_Wrist = base.spaceLocator( n = 'Loc_R_Wrist')
            base.scale(0.1,0.1,0.1, R_Wrist)
            base.parent(R_Wrist, R_Elbow)
            

            #move upper arm
            base.move(0.35 * side, 1 + 0.25 * base.intField(spineJointsCount, query = True, value = True), 0, R_arm)
            base.move(0.6 * side, 1.4, -0.2, R_Elbow)
            base.move(0.8 * side, 1, 0, R_Wrist)
            
            createHands(side, R_Wrist)
            

##### Hands #####        
def createHands(side, wrist):
    if side == 1:
        if base.objExists('L_Hand_GRP'):
            print('L_Hand_GRP already exists')
        else:
            hand = base.group(em=True, name='L_Hand_GRP')
            pos = base.xform(wrist, q=True, t=True, ws=True)
            base.move(pos[0], pos[1], pos[2], hand)
            base.parent(hand, 'Loc_L_Wrist')
            for i in range(base.intField(fingerCount, query=True, value=True)):
                createFingers(1,pos,i)
                
           
                
    else:
        if base.objExists('R_Hand_GRP'):
            print('R_Hand_GRP already exists')
        else:
            hand = base.group(em=True, name='R_Hand_GRP')
            pos = base.xform(wrist, q=True, t=True, ws=True)
            base.move(pos[0], pos[1], pos[2], hand)
            base.parent(hand, 'Loc_R_Wrist')
            for i in range(base.intField(fingerCount, query=True, value=True)):
                createFingers(-1,pos,i)
                
            
               
    
def createFingers(side, handPos, count):
    ## we want to add four finger joints, knuckle/two 'bending joints' and the tip of the finger
    for x in range(0,4):
        ## check which side we're working on, 1 == Left side
        if side == 1:
            ## add a new spaceLocator and name it 'Loc_L_Finger_(number of which finger we're working on.. 0/1/2/etc)_x ( so the for loop above with 0/1/2/3').. the output would be Loc_L_Finger_0_0 for example
            finger = base.spaceLocator(n = 'Loc_L_Finger_' + str(count) + '_' + str(x))
            base.scale(0.05, 0.05, 0.05, finger)
            ## if its the first locator we want to parent it to the hand, the next locators should be parented to the previous locator... locator 0 to the wrist, locator 1 to locator 0 etc
            if x == 0:
                base.parent(finger, 'Loc_L_Wrist')
            else:
                ## if it is not the first locator, parent it to the previous locator (x - 1)
                base.parent(finger, 'Loc_L_Finger_' + str(count) + '_' + str(x - 1))
            ## move it based on which locator it is (x) first locator is * 0 (x), second by 1 etc    
            base.move(handPos[0] + (0.1 + (0.1 * x)) * side, handPos[1] - (0.1 + (0.1 *x)), handPos[2] + -(0.05 * count), finger)
        else:        
            finger = base.spaceLocator(n = 'Loc_R_Finger_' + str(count) + '_' + str(x))
            base.scale(0.05, 0.05, 0.05, finger)
            if x == 0:
                base.parent(finger, 'Loc_R_Wrist')
            else:
                base.parent(finger, 'Loc_R_Finger_' + str(count) + '_' + str(x - 1))
            base.move(handPos[0] + (0.1 + (0.1 * x)) * side, handPos[1] - (0.1 + (0.1 *x)), handPos[2] + -(0.05 * count), finger)
            
            
            
def createLegs(side):
    if side == 1:
        if base.objExists('Loc_L_Grp'):
            print('Loc_L_Leg already exists')
        else:
            L_upperLegGRP = base.group(em=True, name='L_Leg_GRP')
            base.parent(L_upperLegGRP, 'Loc_ROOT')
            base.move(0.1, 1, 0, L_upperLegGRP)

        L_upperLeg = base.spaceLocator(n='Loc_L_UpperLeg')
        base.scale(0.1, 0.1, 0.1, L_upperLeg)
        base.move(0.15, 1, 0, L_upperLeg)
        base.parent(L_upperLeg, 'L_Leg_GRP')

    else:
        if base.objExists('Loc_R_Grp'):
            print('Loc_R_Leg already exists')
        else:
            R_upperLegGRP = base.group(em=True, name='R_Leg_GRP')
            base.parent(R_upperLegGRP, 'Loc_ROOT')
            base.move(-0.1, 1, 0, R_upperLegGRP)

        R_upperLeg = base.spaceLocator(n='Loc_R_UpperLeg')
        base.scale(0.1, 0.1, 0.1, R_upperLeg)
        base.move(-0.15, 1, 0, R_upperLeg)
        base.parent(R_upperLeg, 'R_Leg_GRP')