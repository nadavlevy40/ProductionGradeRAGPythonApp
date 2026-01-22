from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Lease Agreement - English Translation', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=11)

    # The translation text
    text = """
UNPROTECTED LEASE CONTRACT
Drawn up and signed in Rishon LeZion, on the _____ day of ______ 2026

BETWEEN:
Yoav Matsliach, ID 311253785
Bat Chen Matsliach, ID XXXXXXXX
(Hereinafter referred to together and separately as "The Landlord") of the first part;
Email: yoav.mats@gmail.com | Mobile: 054-6626054

AND:
________________, ID ________________
________________, ID ________________
Whose address for the purpose of this agreement is the Leased Property
(Hereinafter referred to together and separately as "The Tenant") of the second part;

WHEREAS: The Landlord is the sole owner and exclusive possessor of a residential apartment located on the 2nd floor, Apt No. 8, at 4 HaPsanter St., Rishon LeZion, known as Parcel 14 in Block 5182 (hereinafter - The Leased Property);

AND WHEREAS: The tenancy is an unprotected tenancy according to the provisions of the Tenant Protection Law (Consolidated Version), 5732-1972 (hereinafter "The Law") and any other tenant protection laws;

AND WHEREAS: It is the Tenant's desire to rent from the Landlord, and the Landlord's desire to rent out to the Tenant, the Leased Property in a general unprotected tenancy, for a limited period as detailed below in accordance with the terms of this agreement;

THEREFORE, IT HAS BEEN AGREED AND STIPULATED BETWEEN THE PARTIES AS FOLLOWS:

--- GENERAL ---
The preamble to this agreement and the attached appendix constitute an integral part hereof. The headings of the clauses in this contract are for reading convenience only and shall not be given any significance in the interpretation of this contract.

--- NON-APPLICATION OF STATUTORY PROTECTION ---
1. The parties declare that the Leased Property is considered a vacant property within its meaning in the provisions of the Law.
2. The Tenant hereby declares and undertakes that:
   - The Leased Property was rented to them for the Lease Period and the Additional Lease Period (if exercised) only, and that the Tenant Protection Law shall not apply to the tenancy.
   - The Tenant has not paid and will not pay in connection with the tenancy under this contract any key money or any other consideration whatsoever other than the Rent specified below.
3. It is agreed that based on the above, the Tenant Protection Law (Consolidated Version), 5732-1972, or any other law that replaces or amends it and grants any protection or privilege notwithstanding the provisions of the lease contract, shall not apply to the tenancy under this contract.

--- CONDITION OF THE LEASED PROPERTY ---
4. The Tenant declares that they have inspected, examined, and seen the Leased Property through the eyes of a tenant and they waive in advance any claim of non-conformity or any other claim regarding the Leased Property.
5. The Tenant further declares that as of the date of signing this lease contract, the Leased Property is in good, intact condition and fit for use, and in this condition, the Leased Property shall be returned to the Landlord upon termination of the Contract in the state of usability and appearance in which it was delivered to them. For the removal of doubt, the Tenant shall not change the color of the walls in the Leased Property, and these shall be returned to the Landlord painted white and free of stains and breaks, unless written approval is received from the Landlord for such a change.

--- PURPOSE OF THE TENANCY ---
6. The Tenant declares that they rented the Leased Property for the purpose of residence for themselves and their nuclear family only and that they will not use the Leased Property except for the aforementioned purpose only.
7. Breach of the provisions of this clause constitutes a fundamental breach of the Agreement.

--- LEASE PERIOD ---
8. The Lease Period is for 18 months only, commencing on 05/02/2026 and ending on 31/08/2026 (hereinafter "The Lease Period").
9. The Tenant has the option to extend the Lease Period for an additional lease period of at least 12 additional months.
10. The Tenant shall be entitled to exercise their right to use the Option Period above by delivering a written notice to the Landlord up to 60 days before the end of the Lease Period, including signing a suitable contract within 10 days of sending the notice, provided they have met all obligations of this contract, including Landlord visits to the Leased Property as requested, and after an agreement for exercising the Option above has been signed between them and the Landlord.

--- SHORTENING THE LEASE ---
11. If the Tenant ceases use of the Leased Property before the end of the Lease Period or Option Period as applicable, without the Landlord's consent, they shall be liable for the full Rent according to this agreement as if they had actually used the Leased Property for the entire Lease Period, up to the amount of Rent for the period the Property was not actually rented. Notwithstanding the above, the Tenant shall be entitled to terminate the lease if they present an alternative tenant to the Landlord's satisfaction, under conditions not inferior to the provisions of this contract and with at least 60 days' notice.

--- RENT ---
12. The Rent for the lease year commencing on 5/2/2026 and ending on 31/8/2027 (hereinafter "The First Lease Period") shall be the sum of 6,000 NIS (Six Thousand New Shekels) for each month of tenancy.
13. The Landlord may raise the Rent during the Option Period at a rate not exceeding 10% compared to the rate in the First Lease Period. Rent for the additional lease year shall be agreed upon after the Tenant announces their intention to exercise the Option.
14. In the event the Tenant is in arrears in paying the Rent for a period exceeding 5 days, the Landlord reserves the right to cancel this contract immediately and evacuate the Tenant from the Leased Property. In any case and without derogating from the above, if the arrears in payment are caused due to non-execution of a payment order, the Landlord shall notify the Tenant and give them a warning of 7 days to effect the payment.
15. Without derogating from the Landlord's right to any other remedy, any payment not paid on time shall bear maximum penalty interest customary at that time at Bank Leumi Le-Israel for debit accounts.
16. The Tenant shall set up a Standing Order in favor of the Landlord, to account name XXXXX in Bank ___, Branch ___, Account Number XXX for the transfer of the monthly payments. Violation of the provisions of the Rent clauses constitutes a fundamental breach of the Agreement.

--- PAYMENTS, EXPENSES, AND NAME TRANSFER ---
17. All expenses, taxes, and levies involved in holding the Leased Property, using it, and enjoying it, which by their nature are imposed on a tenant, for the duration of the Lease Period and Option Period above, including electricity payments, House Committee (Va'ad Bayit), gas, water, and municipal taxes (Arnona), shall apply to the Tenant and be paid by them in full commencing from the date this contract comes into effect, but excluding House Committee payments that are not regular and ordinary payments for maintaining the common property and any other payment which by its nature applies to the owners of the Leased Property, such as levies of various kinds, etc.
18. The Tenant undertakes to pay all payments applying to them on time and to furnish the Landlord, within 5 days of their demand, with receipts and confirmations of the execution of said payments.
19. The Tenant undertakes to notify the Rishon LeZion Municipality, within 7 days of this contract coming into effect, and/or any authority by law relevant to this contract, of the existence of this contract and to transfer the name of the payer of Arnona, water, electricity, gas, and/or any other payment from the Landlord's name to the Tenant's name. The Tenant shall present to the Landlord confirmations of the transfer of charges to their name as stated up to 30 days from the signing of this contract.

--- PROHIBITION OF TRANSFER ---
20. The Tenant is not entitled to transfer their right under this contract to any person or legal entity whatsoever, or to pledge the tenancy or to permit anyone else to use the Leased Property, in whole or in part, in any form whatsoever, whether for consideration or without consideration, without the Landlord's permission in advance and in writing. Notwithstanding the above, the Tenant may bring into the Leased Property employees on their behalf for the purpose of managing and operating the Leased Property and holding any regular and reasonable hosting activity. For the removal of doubt, the Tenant is forbidden to sublet the Leased Property.

--- PROHIBITION OF CHANGES ---
21. The Tenant shall not be entitled to make any change whatsoever and any addition whatsoever in the Leased Property or outside it, without exception, whether it is a structural change or any other change and even if it improves the Leased Property, unless express consent has been given for this in advance and in writing by the Landlord and under those conditions agreed upon. Except for all detailed additions approved by the Landlord detailed in Appendix A to this agreement. Breach of this clause constitutes a fundamental breach of the Agreement.
22. Without derogating from the above, it is hereby agreed that any change, improvement, or addition whatsoever performed in the Leased Property on behalf of the Tenant shall be considered the property of the Landlord; however, the Landlord shall be entitled to demand the Tenant remove from the Leased Property any such change or addition at the Tenant's expense and restore the condition of the Leased Property to its previous state, such that the Leased Property shall be fit for immediate use and tenancy, immediately upon the end of the Lease Period or the Option as applicable. Breach of this clause constitutes a fundamental breach of the Agreement.

--- SAFEKEEPING OF THE LEASED PROPERTY ---
23. The Tenant declares that the Leased Property was delivered to them with the items detailed below:
   - Mini central air conditioner, Electric water heater
   - Gas cooktop, Modern integral wardrobe in the bedroom
   - Garden furniture set (on the balcony), Gas grill + cylinder (on the balcony)
24. It is clarified that any damage or malfunction caused to the Leased Property and/or contents, arising from reasonable and ordinary wear and tear and not arising from damages caused as a result of negligent use and/or malice and/or omission by the Tenant in safeguarding them and/or using them, shall be borne by the Landlord who shall take care to repair them within a reasonable time under the circumstances from the time they became aware of the defect and/or flaw and/or bear the expenses of their repair. (Damages such as flooding, short circuits, etc., will be repaired immediately where possible, subject to receiving notice from the Tenant).
25. The Tenant undertakes to use the Leased Property and the chattels within it in a careful and reasonable manner, to refrain from any use likely to cause damage or malfunction whatsoever to the Leased Property and/or chattels therein and/or to the building and/or to the Landlord and/or to any third party found in the Leased Property, to take all necessary safety measures paying attention to the use made of the Leased Property, and to repair at their expense within a reasonable time under the circumstances any damage, defect, and malfunction arising from damages caused as a result of negligent use and/or malice and/or omission by the Tenant.
26. It is agreed that any damage to electrical equipment, namely air conditioners, electric shutters, and plumbing, the repair cost of which is up to 500 NIS, shall apply to the Tenant. It is the Landlord's responsibility to complete any amount required to repair the said equipment above the amount stated in this clause. It is agreed that the Landlord shall repair at their expense any moisture damages formed in the apartment.
27. In any case, the Tenant shall notify the Landlord of any malfunction, breakdown, defect, or loss in connection with the Leased Property immediately upon their formation or discovery.
28. The Tenant undertakes to compensate the Landlord and indemnify them for any damage or expense caused to the Landlord due to any claim submitted against the Landlord arising from non-fulfillment of any obligation of the Tenant under this agreement or due to the behavior of the Tenant and/or anyone on their behalf.

--- VACATING AND RETURNING POSSESSION ---
30. At the end of the Lease Period under this contract and/or in any event of cancellation of the contract, the Tenant undertakes to vacate the Leased Property and return possession thereof to the Landlord with the Leased Property in good and proper condition as they received it, clean, with walls, wall cupboards, and doors clean and intact. It is the Landlord's responsibility to paint walls and/or doors whose paint is damaged. All plumbing fixtures and electrical equipment - AC, water heater, electric shutter - intact.
31. Upon vacating, or at the end of the Lease Period, the Tenant shall not be entitled to receive any payment whatsoever as key money or any other benefit, in any way, in exchange for vacating and returning possession to the Landlord, and they may not remain in the Leased Property after the end of the Lease Period.
32. At the end of the Lease Period under this contract and/or in any event of cancellation of the contract, the Tenant undertakes to vacate the Leased Property and return possession thereof to the Landlord without any debts and fit for immediate use.
33. It is agreed between the parties that restoring the Leased Property to its previous state at the time of the end of the Lease Period or in any other case means restoring it clean and free of any object and person, except for chattels belonging to the Landlord.
34. At the time of vacating the Leased Property and delivering possession thereof to the Landlord, the Leased Property shall be inspected by the Landlord and a delivery protocol shall be signed by both parties regarding the termination of the parties' obligations under the Contract. If at this time open accounts for payment remain, the Tenant shall pay the Landlord according to an estimate the balance of open accounts relative to previous accounts of the Leased Property. Upon receipt of exact accounts, the parties shall pay one another account differences as required. At this time, as long as the Tenant presents confirmations of covering their debts to the authorities, the House Committee, the gas company, the electric company, and the water corporation, the Landlord shall return to the Tenant the securities delivered to the Landlord at the time of signing the Contract.

--- OBSERVANCE OF LAW ---
35. Within the framework of using the Leased Property, the Tenant undertakes to strictly fulfill all provisions of the Law, bylaws, regulations, custom, and accepted instructions, and to refrain from any harassment, nuisance, or damage to any other tenants, subject to the purpose of the tenancy stated above.

--- REFUND OF PAYMENTS / REPAIRS ---
36. Any amount paid by any party the payment duty of which applies to the other party, shall be refunded by the latter to the former upon first demand, linked to the Consumer Price Index and bearing interest according to law within 7 days from the day of notice.
37. Breach of the provisions of this clause constitutes a fundamental breach of the Agreement. The Tenant shall not be entitled to offset amounts they owe the Landlord by virtue of this lease agreement.
38. Without derogating from the provisions of this agreement, it is agreed that if during the tenancy fundamental defects are discovered and/or formed anywhere in the Leased Property structure which do not arise directly from an act or omission done in the Leased Property by the Tenant and/or with their consent and/or authorization and/or responsibility (e.g., bursting of a main water pipe of the building etc., which does not stem from negligent use by the Tenant), the Landlord must repair them within a reasonable time under the circumstances from the time they became aware of the defect and/or flaw and/or bear the expenses of their repair.
39. Damages that do not allow reasonable living in the Leased Property shall be repaired where possible immediately, subject to giving notice from the Tenant.
40. In such a case, the Tenant undertakes to notify the Landlord immediately regarding the defect requiring repair, if any, to allow them or their representatives to perform the necessary repair. Nothing in this clause constitutes granting authorization to the Tenant to perform repairs as above without the Landlord's consent in advance and in writing. Notwithstanding the provisions of this clause and clause 39, insofar as the Landlord does not act to repair the defects and the said defects do not allow reasonable living in the Leased Property, the Tenant has the right to repair them themselves or by someone on their behalf.
41. The Landlord undertakes to pay the cost of the repair within seven working days and subject to the presentation of payment receipts on the part of the Tenant. Breach of this clause is a fundamental breach of the Agreement.

--- LANDLORD'S INSPECTION ---
42. Permission is granted to the Landlord by their representative and any person appointed by them, to visit the Leased Property, occasionally at regular times and hours including Fridays and with prior coordination, for the purpose of checking fulfillment of the provisions of this contract and/or to show the Leased Property to other buyers or tenants and/or for the purpose of performing repairs and works in the area where the Leased Property is found, and the Tenant must allow the Landlord to enter the Leased Property and any part thereof and do there any action as needed, with prior coordination.
43. In case of emergency and/or danger to human life and/or integrity of the Leased Property, the Landlord may enter the Leased Property immediately at any time.
44. If the Tenant has not delivered notice of their intention to extend the Lease Period, the Landlord shall be entitled during the period of 60 days before the end of the Lease Period or the Option as applicable, to show the Leased Property to another potential tenant, in prior coordination with the Tenant. As long as the frequency of visits to the Leased Property does not cause a nuisance and/or disturbance to the Tenant's daily routine.
45. The Tenant undertakes to present to the Landlord confirmations regarding the settlement of all payments they are liable for settling under the provisions of this contract, within 7 days from the date of the Landlord's first demand. Breach of this clause constitutes a fundamental breach of the Agreement.

--- CANCELLATION OF TENANCY ---
46. Without derogating from their rights under any law and under this agreement, each party shall be entitled to cancel this agreement and demand the evacuation of the Leased Property even before the end of the Lease Period if:
   - One of the parties breached a fundamental breach or did not fulfill a fundamental stipulation of the stipulations of this contract, and did not correct the breach within 7 days from the day they were asked to do so.
   - A request for receivership or bankruptcy was filed against the Tenant. The Tenant was declared a debtor of limited means.

--- AGREED COMPENSATION ---
47. In addition to any remedy and relief available to the Landlord under the stipulations of this contract or the provisions of the Contracts Law (Remedies for Breach of Contract), 5731-1971, or under any law, if the Tenant does not vacate the Leased Property and does not return possession thereof to the Landlord at the end of the Lease Period or the Option as applicable, or upon cancellation of the contract prior thereto, then the Tenant shall pay the Landlord agreed compensation, fixed and estimated in advance, at an agreed rate equal to 600 NIS (Six Hundred New Shekels) for every day of arrears in delivering possession of the Leased Property, without derogating from any remedy given to the Landlord in accordance with the provisions of this agreement and/or in accordance with the provisions of any law.
48. Nothing in this clause shall be interpreted as detracting from the Landlord's right to take all legal measures in order to evict the Tenant and/or anyone on their behalf from the Leased Property at the said time and/or for any other remedies under the law and/or this agreement. For the removal of doubt, the above pre-agreed compensation was determined by the parties based on a weighed, careful, and objective estimation of the damages that will be caused to the Landlord as a result of delay in vacating the Leased Property and it is agreed that the Landlord shall be entitled to receive this compensation without need for proof of their damages and the claim by the Tenant that this compensation was determined as a fine shall not be heard.

--- SEIZING POSSESSION BY THE LANDLORD ---
49. Without derogating and/or harming the Landlord's rights under this agreement, in addition to any other remedy and relief given to the Landlord under any law, the Landlord shall be entitled, in case of non-evacuation of the Leased Property by the Tenant at the end of the Lease Period or upon cancellation of the contract, to enter the Leased Property in any way they see fit and to take all measures for the purpose of evicting the Tenant from the Leased Property, and shall also be entitled to store in any place they see fit and at the Tenant's expense, any object of the Tenant's objects found in the Leased Property, while the Landlord shall be considered for any need and matter as an unpaid bailee.
50. The Tenant hereby authorizes and empowers the Landlord to act in the manner and form stated above irrevocably and non-cancellably.
51. After the date fixed or to be fixed for evacuation (whether at the end of the Lease Period or at any other date), the Tenant shall be considered for any need and matter as a holder unlawfully in the Leased Property.

--- CHANGE OF CONTRACT ---
52. Any previous lease agreement and/or memorandum of understanding signed between the parties is null and void and the provisions of this agreement replace it.
53. It is hereby expressly agreed and declared that any change, addition, or deviation from the stipulations of this agreement shall be done in writing and signed properly by the parties.

--- APPLICABILITY ---
54. This lease contract shall come into force commencing from the day of its signing.
55. At the beginning of the Lease Period and at its end, the parties shall record and confirm the reading of the electricity and water meters, for the purpose of checking the accounting between them. A delivery protocol shall be signed between the parties at the two dates above wherein the meter readings as stated shall be recorded.

--- SECURITIES (COLLATERAL) ---
56. At the status of signing this agreement, the Tenant shall deposit in the Landlord's hands a Bank Check to the order of the Landlord - for the beneficiary only, in the sum of 20,000 NIS without a repayment date, to guarantee the Tenant's obligations under this contract, including payments that may be due to the Landlord due to damages caused, if caused to the Leased Property by the Tenants and/or anyone on their behalf and/or due to non-evacuation of the Leased Property on time and/or agreed compensation and/or due to non-payment of any of the payments the Tenant is liable for under this agreement.
57. In addition, the Tenant shall give the Landlord 4 signed checks without an amount listed to the name of:
   - The House Committee at 4 HaPsanter St., Rishon LeZion
   - Rishon LeZion Municipality - Collection Department
   - Pazgas Company
   - Manifesto Rishon Water Corporation
58. Breach of the provisions of this clause constitutes a fundamental breach of the Agreement.
59. The Landlord undertakes to return the checks deposited in their hands at the end of the Lease Period or Option and no later than the date of presenting confirmations of full and final settlement of all accounts the Tenant is liable for regarding their use of the Leased Property and/or regarding their obligations under this agreement, and subject to vacating the Leased Property and delivering possession thereof to the Landlord as stated in this agreement and signing a delivery protocol by the parties. For the removal of doubt, security monies shall be returned without any linkage differentials or interest whatsoever.
60. The Tenant empowers the Landlord to fill these checks if a debt is created and this only if after seven days from the day of sending a written notice to the Tenant, the Tenant has not corrected the breach noted in the warning letter.
61. It is clarified that the Landlord shall not bear any responsibility whatsoever for damages caused to the body and/or property of the Tenant and/or their visitors and/or invitees and/or employees due to use of the Leased Property. If any claim is filed against the Landlord, the Tenant undertakes to indemnify the Landlord for any amount claimed and/or paid due to this, including expenses and attorney's fees.

--- REPLACEMENT OF LANDLORD ---
62. The Landlord is entitled to transfer their rights under this agreement or any part thereof to another, including by way of selling the Leased Property, provided that the Tenant's rights under this agreement are not harmed and all Tenant's obligations towards the Landlord continue to apply regarding any substitute of the Landlord.
63. The Tenant undertakes to sign any document required, if required, in connection with the transfer of the Landlord's rights in the Leased Property, and to show the Leased Property to potential buyers and/or potential tenants, in prior coordination with the Tenant at least 3 times a week at times that do not amount to an unreasonable nuisance.
64. Breach of the provisions of this clause constitutes a fundamental breach of the Agreement.

--- MISCELLANEOUS ---
65. The addresses of the parties for the purposes of this agreement are as detailed in the preamble to this agreement. Any notice sent by registered mail shall be considered as if delivered to its destination at the end of 72 hours from the time of its dispatch, and if delivered by hand at the time of its delivery.


SIGNATURES:
The Landlord: __________________________
The Tenant:   __________________________


--- GUARANTEE DEED ---

The Guarantor signed below declares and undertakes hereby that they guarantee personally, unconditionally, and irrevocably, the fulfillment of all obligations of the Tenant under this lease agreement, including but not limited to: payment of Rent in full and on time, accompanying payments applying to the Tenant (including Arnona, water, electricity, gas, House Committee, etc.), compensation for damages to the apartment, installations, and equipment therein, and any other charge that applies to the Tenant by virtue of this agreement and/or by virtue of any law.

The Guarantor declares that they are in personal contact with the Tenant and that their guarantee is given out of full familiarity with the Tenant and their ability to meet their obligations under this agreement.

The Guarantee is a continuing guarantee, applying to the entire Lease Period and any extension, renewal, or continuation of the tenancy, even if a new agreement is not signed, and shall remain in force until full, final, and absolute settlement of all Tenant's obligations towards the Landlord.

The Guarantor waives in advance and explicitly any claim and/or demand that the Landlord must first address the Tenant and/or take any proceedings against them, and agrees that the Landlord shall be entitled to address them directly and demand from them the fulfillment of obligations and/or payment of any amount due from the Tenant under this agreement.

The Guarantor declares that they have read the Lease Agreement, understood its content and the significance of their obligations as a Guarantor, and that they sign this Guarantee Deed of their own free will.

Guarantor's Details and Signature:
Full Name: ________________
ID: ________________
Relation to Tenant: ________________
Address: ________________
Telephone: ________________
Guarantor's Signature: ________________
Date: ________________
    """

    # Replace special symbol that standard fonts don't like
    text = text.replace("₪", "NIS")
    
    # Write text
    pdf.multi_cell(0, 8, text)
    
    # Save
    pdf.output("translated_contract.pdf")
    print("PDF Generated successfully: translated_contract.pdf")

if __name__ == "__main__":
    create_pdf()