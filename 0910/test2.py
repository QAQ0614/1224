article = """
Other nuke deal nations craft plan to keep doing business with Iran
UNITED NATIONS -- Five world powers and Iran agreed late Monday to establish a financial facility in the European Union to facilitate payments for Iranian imports and exports including oil, a key move sought by Tehran following the U.S. pullout from the 2015 nuclear deal and its re-imposition of sanctions. Foreign ministers from Britain, France, Germany, Russia, China and Iran said in a joint statement that the so-called "Special Purpose Vehicle" will "assist and reassure economic operators pursuing legitimate business with Iran."
The nuclear agreement, formally known as the Joint Comprehensive Plan of Action (JCPOA) is meant to prevent Tehran from developing nuclear weapons, but U.S. President Donald Trump announced in May he was unilaterally pulling out because he felt it wasn't strong enough and didn't cover other issues of concern to the U.S. and its allies, such as Iran's military influence in the Middle East and ballistic missile program. The U.S. has also accused Iran of promoting international terrorism, which Tehran vehemently denies.
Iran's economy is already suffering from the sanctions that Washington re-imposed after walking away from the nuclear agreement, and the U.S. has threatened to punish companies from other nations that continue doing business with Iran.
In sharp contrast, the five other world powers who signed the nuclear deal remain strongly committed to it, and the new financial facility is almost certain to anger the Trump administration.
Earlier this week, before heading to the United Nations General Assembly in New York, British Prime Minister Theresa May told "CBS This Morning" co-host John Dickerson that she trusts Mr. Trump, but believes Iran is holding up its end of the nuclear deal.
"I do have a difference of opinion with President Trump, because we (Britain) believe the JCPOA should stay in…place. And others involved in putting that deal together believe that it should stay in place. We do agree with the United States that there are other aspects of Iran's behavior that we need to be dealing with, too. So looking at the issue of ballistic missiles. Looking at the way in which Iran is acting in the region to destabilize the region. We need to address those issues, too. But we also want to ensure that we have a nuclear deal in place that prevents them from, of getting a nuclear weapon."
"The important thing about the JCPOA," said May, "is that it is still in place. Yes, the United States has taken a particular view on how to deal with this issue. That's a view which we disagree with. We take a different view. But that deal is still in place."
The Trump administration has been pushing its allies around the world to stop buying Iranian oil for months, but as of August it had received no firm commitments from the biggest purchasers of Iranian petroleum products to find other suppliers. May's interview with Dickerson came on the heels of a fresh warning from U.S. Ambassador to the U.N. that Britain and other nations doing business with Iran would not be given any passes.
Asked on "Face the Nation" whether remaining signatories of the nuclear pact could face U.S. penalties for continued business relationships with Iran, Haley said those countries would have to weigh the benefit of dealing with Iran against the risk of U.S. sanctions. 
"The Europeans have a decision to make. And I think that decision is already being made. If you look, they are dropping business from Iran left and right," Haley said. "We will have decisions to make in terms whether they get exemptions or not, but I'll tell you right now, we're going to be really tough on Iran. We're not giving them a pass."
European Union foreign policy chief Federica Mogherini told reporters after the closed-door ministerial meeting that the financial facility is aimed in part at preserving the nuclear agreement. The EU and Iran say the deal is working, and the joint statement notes that the International Atomic Energy Agency has now certified 12 times that Iran is in compliance with its obligations.
"In practical terms," Mogherini said, "this will mean that EU member states will set up a legal entity to facilitate legitimate financial transactions with Iran and this will allow European companies to continue to trade with Iran in accordance with European Union law and could be open to other partners in the world."
She said the agreement follows extensive exchanges and announced that a meeting of technical experts will be held to "operationalize" the new financial facility.
The joint statement said the six countries that signed the 2015 nuclear agreement "reconfirmed their commitment to its full and effective implementation in good faith and in a constructive atmosphere." They called the agreement "a key element of the global non-proliferation architecture and a significant achievement of multilateral diplomacy."
The participants reaffirmed their joint statement on July 6, "in particular to pursue concrete and effective measures to secure payment channels with Iran."
"""

count = 0
for c in article:                          
    if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  
         caps = caps + 1
    elif c in "abcdefghijklmnopqrstuvwxyz":
        lowers += 1
    else: c in "0123456789"
        others += 1

        count = count + 1                   

print(count)  
