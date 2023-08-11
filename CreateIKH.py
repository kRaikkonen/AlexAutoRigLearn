import maya.cmds as base

def IKHandles():
    
    if not base.objExists("RIG_L_ArmTwist_"):
        base.ikHandle(name="IK_L_Arm", sj=base.ls("RIG_L_UpperArm")[0], ee=base.ls("RIG_L_Wrist")[0], sol='ikRPsolver')
        base.ikHandle(name="IK_R_Arm", sj=base.ls("RIG_R_UpperArm")[0], ee=base.ls("RIG_R_Wrist")[0], sol='ikRPsolver')
    else:
        base.ikHandle(name="IK_L_Arm", sj=base.ls("RIG_L_UpperArm")[0], ee=base.ls("RIG_L_ArmTwist_0")[0], sol='ikRPsolver')
        base.ikHandle(name="IK_R_Arm", sj=base.ls("RIG_R_UpperArm")[0], ee=base.ls("RIG_R_ArmTwist_0")[0], sol='ikRPsolver')
        
        
        leftWristPos = base.xform(base.ls("RIG_L_Wrist"), q = True, t = True, ws = True)
        rightWristPos = base.xform(base.ls("RIG_R_Wrist"), q = True, t = True, ws = True)
        
        leftIK = base.ikHandle(base.ls("IK_L_Arm", q = True, ee = True))
        rightIK = base.ikHandle(base.ls("IK_R_Arm", q = True, ee = True))
        
        base.move(leftWristPos[0],leftWristPos[1],leftWristPos[2], leftIK+".scalePivot")
        base.move(rightWristPos[0],rightWristPos[1],rightWristPos[2], rightIK+".scalePivot")
        
        
    
    
    base.ikHandle(name="IK_L_Leg", sj=base.ls("RIG_L_UpperLeg")[0], ee=base.ls("RIG_L_Foot")[0], sol='ikRPsolver')
    base.ikHandle(name="IK_R_Leg", sj=base.ls("RIG_R_UpperLeg")[0], ee=base.ls("RIG_R_Foot")[0], sol='ikRPsolver')
    
    base.ikHandle(name="IK_L_Ball", sj=base.ls("RIG_R_Foot")[0], ee=base.ls("RIG_R_Ball")[0], sol='ikSCsolver')
    base.ikHandle(name="IK_R_Ball", sj=base.ls("RIG_R_Foot")[0], ee=base.ls("RIG_R_Ball")[0], sol='ikSCsolver')

    base.ikHandle(name="IK_L_Toes", sj=base.ls("RIG_R_Ball")[0], ee=base.ls("RIG_R_Toes")[0], sol='ikSCsolver')
    base.ikHandle(name="IK_R_Toes", sj=base.ls("RIG_R_Ball")[0], ee=base.ls("RIG_R_Toes")[0], sol='ikSCsolver')



    #######################
    rootPos = base.xform(base.ls("RIG_ROOT", type = 'joint'), q = True, t = True, ws = True)
    spines = base.ls("RIG_SPINE_*", type = 'joint')
    
    spinePos = []
    
    for i, sp in enumerate(spines):
        spinePos.append(base.xform(spines[i], q = True, t = True, ws = True))
        
        
    base.curve( p = [(rootPos[0], rootPos[1], rootPos[2])], n = "SpineIKCurve", degree = 1)    

    for j, sp in enumerate(spinePos):
        base.curve('SpineIKCurve', a = True, p = [(spinePos[j][0], spinePos[j][1], spinePos[j][2])])
        
    
    curveCV = base.ls('SpineIKCurve.cv[0:]', fl = True)
    
    for k, cvs in enumerate(curveCV):
        c = base.cluster(cvs, cvs, n = "Spine_Cluster_"+str(k)+"_")
        if k > 0:
            base.parent(c,"Spine_Cluster_"+str(k-1)+"_Handle")
    
    if(base.objExists("Loc_SPINE_*")):
        spineAmount = base.ls("Loc_SPINE_*", type = 'transform')
    else:
        spineAmount = base.ls("RIG_SPINE_*") 
    
    base.ikHandle(n = "IK_Spine", sj = "RIG_ROOT", ee = "RIG_SPINE_" + str(len(spineAmount) - 1), sol = 'ikSplineSolver', c = 'SpineIKCurve', ccv = False)    