# Add another list having occ2
def dict():
  #All occurences 1 lists-
  
  list_BindAgg = [
    "Binding Agreement", "Contractual obligation",
    "Legally binding commitment", "Enforceable contract", "Approved settlement"
  ]

  list_PurPrc = [
    "Purchase Price", "Purchasing Price", "Acquisition expense",
    "Procurement fee", "Sale price", "Sales Price", "Acquisition cost",
    "Purchase amount"
  ]
  
  list_ShllPay = [
    "Shall Pay", "Must pay", "Is obligated to pay", "Agrees to remit payment",
    "Pledges to remunerate", "Vows to reimburse", "Promises to meet the cost."
  ]
  
  list_mrkt = ["market", "mkt"]
  list_sus = ["Sustainable", "Sustainability"]
  list_indm = ["Indemnify", "Indemnification", "Indemnified", "Indemnifying"]
  list_ForMaj = [
    "Force Majeure", "Force Majore", "Act of God", "Acts of God",
    "Cas Fortuit", "Superior Force", "Unforeseeable Circumstances",
    "Vis Major", "Irresistible Force", "Unavoidable Accident",
    "Elemental Forces", "Acts of Nature", "Uncontrollable Circumstances",
    "Major Force", "Unforeseen Events", "Civil Disturbance",
    "War or Terrorism", "Government Intervention"
  ]

  #=================================================================================================#



#===================================================================================================#
#ALL OCCURENCES 2 ''''
  
  list2_BindAgg=["Binding Agreement", "Contractual obligation",
      "Legally binding commitment", "Enforceable contract", "Approved settlement"]
  list2_PurPrc=["$","1","2","3","4","5","6","7","8","9"]
  list2_ShllPay=["$","1","2","3","4","5","6","7","8","9"]
  list2_mrkt=["market", "mkt"]
  list2_sus=["Sustainable", "Sustainability"]
  list2_indm=["Indemnify", "Indemnification", "Indemnified", "Indemnifying"]
  list2_ForMaj=["Force Majeure", "Force Majore", "Act of God", "Acts of God",
      "Cas Fortuit", "Superior Force", "Unforeseeable Circumstances",
      "Vis Major", "Irresistible Force", "Unavoidable Accident",
      "Elemental Forces", "Acts of Nature", "Uncontrollable Circumstances",
      "Major Force", "Unforeseen Events", "Civil Disturbance",
      "War or Terrorism", "Government Intervention"]
  
  
  dict = {
      "BindAgg": [list_BindAgg,list2_BindAgg],
      "PurPrc": [list_PurPrc,list2_PurPrc],
      "ShllPay": [list_ShllPay,list2_ShllPay],
      "mrkt": [list_mrkt,list2_mrkt],
      "sus": [list_sus,list2_sus],
      "indm": [list_indm,list2_indm],
      "ForMaj": [list_ForMaj,list2_ForMaj]
    }


  return dict
  