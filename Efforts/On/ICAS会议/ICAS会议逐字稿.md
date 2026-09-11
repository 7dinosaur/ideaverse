**Slide 1**
Dear experts and colleagues

I am Lin Yi from Northwestern Polytechnical University. 

It is a great honor to present our work today — "Low-Boom Design and Analysis of a Blended-Wing-Body Configuration for Large-Sized Supersonic Transport."

**Slide 2**
My presentation consists of four parts: 

first, research background and motivation; 

second, generation of the baseline configuration; 

third, low-boom design and analysis; 

and finally, summary and outlook.

**Slide 3**
Faster travel improves the efficiency of global economic and cultural exchange. 

Supersonic transport fly more than twice as fast as subsonic airliners and are regarded as a core technological frontier of the 21st-century aviation industry. 

NASA's 2023 strategic plan states that "efficient, affordable, and environmentally friendly supersonic commercial transport will be a gamechanger for future intercontinental travel." 

Supersonic transport is therefore one of the frontier topics in aviation.

**Slide 4**
However, strong sonic boom restricts the practical operation of supersonic transport. 

To address this problem, many advanced low-boom configurations have been developed worldwide over the past decades, such as NASA's X-59, Lockheed Martin's QSTA, TsAGI's Strizh, and JAXA's S4. 

We found that most of them have small capacity, they are all small bussiness jet. 

Under the classical sonic boom theory, the theoretical minimum sonic‑boom level is strongly correlated with aircraft weight. It is evident that smaller‑capacity are more available for satisfying low‑boom constraints. 

But, a smaller capacity usually means higher ticket fares, since the expensive operating cost of supersonic transport will spread over very few passengers. 

In contrast, carrying more passengers per flight will significantly decreases the operating cost shared by each passenger, then the ticket fare will be reduced.

**Slide 5**
So what about upsizing the aircraft? 

This shows the cabin and fuselage cross‑section of a supersonic transport. Now if we double the number of seats, the fuselage cross‑sectional area will grow quadratically and have more redundant space. 

Double passengers, 4 times area, 4 times volume, and in existing low-boom theory the volume is directly associated with the low boom target, if we need more fuselage volume for the cabin constraint, that means the low boom design space is significantly limited. 

The key point is tranditional configuration's circular fuselage are poor at turning volume into passenger capacity. I call this volume efficiency, and it is low for tranditional configuration. 

So what configuration gives us high volume efficiency?

**Slide 67**
Naturally we come out the Blended-Wing-Body configuration. BWB configuration are generally considered to have higher loading efficiency. 

Let’s make a comparison. With 4 seats 1 row in both cases, the BWB configuration's cross-section better conforms to the cabin, and has less redundant space. Volume is converted more effectively into seating capacity. 

Meanwhile, comprehensive research on BWB already exists for subsonic applications. Compared with other innovative configurations, it benefits from more mature technologies that can be reused.

**Slide 8**
Therefore, we proposes a 160-seat supersonic BWB configuration and systematically examines its feasibility and low-boom design potential through three tasks: 

analyzing its aerodynamic and sonic boom characteristics; 

performing forebody signature design with the classical JSGD inverse design method; 

and studying the effects of winglet and V-tail on the aft body waveform.

**Slide 9**
So, first we need to define the geometry of cabin so that we can establish the cabin constraint in subsequent design. 

We set 40 rows with four seats per row to accommodate 160 passengers. 

In a TAW configuration the cabin ceiling is curved and cannot serve as passenger space, so it is occupied by carry-on baggage. 

In SBWB, a relatively complete rectangular cabin can be used: square overhead bins are more convenient, or the bins can be removed to give passengers more vertical space and improve comfort.

**Slide 10**
For TAW configuration, the fuselage and wing are often designed separately. But the SBWB requires an integrated design. 

So we use a full-aircraft CST parameterization method: all sections are parameterized by CST functions of the same order. 

For the fuselage region, we fit CST parameters to enclose the predefined cabin. For the wing, CST parameters of thin supersonic airfoils are directly adopted.

Then adjacent sections are blended by third-order NURBS interpolation to construct the aerodynamic surface, NURBS method can guarantee the geometric smoothness.

**Slide 11**
Therefore we get the baseline configuration, Here presents the three‑view drawing.

The cruise condition is set at 18 km and Mach 1.8. The takeoff weight is 170 ton, with about 20 ton of fuel burned before entering cruise, giving a cruise weight of 150 ton.

**Slide 12**
Then we performed a aerodynamic evaluation of the baseline configuration:

the cruise angle of attack is 4.1 degrees, the lift coefficient 0.107 and the lift-to-drag ratio is 11.2. By analyzing the drag components, it can be found that pressure drag accounts for 62.2% and viscous drag 37.8%, the drag is mainly volume-driven. 

From the pressure distribution, the low-pressure region on the SBWB appears earlier than on the TAW configuration: the TAW adopts a sharp slender nose to control sonic boom, so lift only begins at wing, whereas the SBWB has more uniform axial lift distribution.

**Slide 13**
Now, analyse the sonic boom characteristics. 

Constrained by the long cabin, the aft fuselage tapers sharply. This rapid volume drop creates strong over‑expansion at the aft‑body.

We extract the near‑field boom signature at three body lengths away.

We can see that SBWB produces a flat‑top forebody signature. This comes from its broader lift distribution and inherent volume‑lift coupling. that's also why we need integrated design method for SBWB.

Then we propagate this near‑field signature down to the ground, the undertrack boom reaches 105.7 PLdB — a level similar to Concorde.

**Slide 14**
Next, the low-boom design, using the classical JSGD inverse design method on the full-aircraft parameterization.

After design, we get a new near‑field waveform, it has a strong nose shock and sloped mid‑waveform.

Propagation result shows that the ground sonic boom intensity is 99.2 PLdB. Compared with the baseline configuration, the boom level decreases by 6.5 PLdB. This indicates that the classical JSGD theory is still effective for the SBWB configuration.

However, the optimized configuration still maintains strong over‑expansion. From the ground waveform, aft‑body over‑expansion dominates the high sonic‑boom intensity.

**Slide 15**
In previous low-boom design studies, those control surfaces like tail wing are generally used for regulating the aft-body waveform, we wondering if those components are also effective in SBWB.

We chose the winglets and V-tails because they are typical components usually adopted for BWB.

This shows the size and shape of the winglet and V-tail. 

Without detailed flight mechanics analysis, its parameters are determined based on experience. 

For the V-tail, its area is calculated according to pitch and lateral-directional moment requirements. 

And a large sweep angle is specially designed to enhance its interference on the aft-body waveform.

**Slide 16**
First, the winglets.

For the mechanism: the low pressure over the wing upper surface propagates to the aft-body via the wing-tip vortices, amplifying the aft-body over-expansion.

The winglets prevent this upper-surface low pressure from intruding onto the lower surface.

So the wingtip vortices are suppressed, and the over-expansion is mitigated.

**Slide 17**
Next, we install the V-tails.

From the pressure distribution, we can observe that shocks generated by the tail surfaces are shielded by the fuselage.

Comparing the near‑field signatures, we find the tail surfaces exert nearly no influence on the aft‑body wave system. This further demonstrates that most of the tail’s effect is shielded by the fuselage.

Althought V-tails have not show a effective influence in this case. but We must note that this is preliminary work, and the V-tail mechanisms are not systematically studied yet.

**Slide 18**
Then, we install both components

The combined effect is not a simple superposition. The two components interfere with each other: the coupling further reduces the aft-body over-expansion, and the shock intensification from the winglets is also suppressed.

As the results show, the ground sonic boom intensity further reduced by 0.5 PLdB.

**Slide 19**
To conclude

First, the SBWB cabin-conformal fuselage enlarges the low-boom design space.

Second, the classic JSGD method remains effective for sonic-boom reduction on the SBWB.

Third, winglets and V-tails enable the regulation of the aft-body over-expansion intensity.

For future work, we will explore canard for fore‑body waveform control, adopt tail shaping to mitigate the over-expansion on the aft‑body, and further extend the SBWB concept to supersonic business jet applications.

**Slide 20**
Thank you for your attention. Questions are welcome!