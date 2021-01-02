'''
************************************************************************************
***^^^^ DANGER WILL ROBINSON *******
************************************************************************************
Calculates how much ivermectine dosage for sheep drench per bodyweight (lbs or kg)
************************************************************************************
***^^^^ DANGER WILL ROBINSON *******
************************************************************************************
THIS IS ONLY A TEST
    DO NOT USE FOR MEDICAL ADVISE
THIS IS ONLY A TEST
    DO NOT USE FOR MEDICAL ADVISE
THIS IS ONLY A TEST
    DO NOT USE FOR MEDICAL ADVISE
THIS IS ONLY A TEST
    DO NOT USE FOR MEDICAL ADVISE
THIS IS ONLY A TEST
    DO NOT USE FOR MEDICAL ADVISE
************************************************************************************
***^^^^ DANGER WILL ROBINSON *******
************************************************************************************
'''

imML_PER_huPOUND    = 0.11538461538
imMG_PER_imML       = 0.8
_LBS_PER_KG         = 2.20462
imMg_PER_huKG       = .2
imML_PER_imMG       = 3/2.4
imMG_PER_imLBS      = imMg_PER_huKG/_LBS_PER_KG

def mg_of_im_per_ml(ml):
    return ml/imML_PER_imMG

def mg_of_im_per_bodyweight(wtKg=None,wtLbs=None):
    if not wtKg and not wtLbs:
        print('Must enter a weight: (wtKg or wtLbs)')
        return 0
    if wtKg:
        return imMg_PER_KG*wtKg
    if wtLbs:
        return imMG_PER_imLBS*wtLbs

def ml_of_im_per_bodyweight(wtKg=None,wtLbs=None):
    mg = mg_of_im_per_bodyweight(wtKg=wtKg,wtLbs=wtLbs)
    return mg*imML_PER_imMG

imMl = 240
mgPerMl = mg_of_im_per_ml(imMl)
wtLbs = 165
doseMg = mg_of_im_per_bodyweight(wtLbs=wtLbs)
print('(%s)ml ivermectin = %.3f (mg)'%(imMl, mgPerMl))
print('(%s)ml ivermectin 1 Dose = %.3f(mg)@%.2f(lbs) =>  %.3f (doses/%.0f(ml))'%(imMl, doseMg, wtLbs, mgPerMl/doseMg, imMl))
print('')

for i in range(10):
    wt = i*25 + 25
    print('---- %.2f lbs'%wt)
    print('   %.3f (mg)  -> %.3f (ml)'%( mg_of_im_per_bodyweight(wtLbs=wt),ml_of_im_per_bodyweight(wtLbs=wt)))
    # print('  (lbs) = '%(wt, ml_of_im_per_bodyweight(wtLbs=wt)))
    # print('----')
