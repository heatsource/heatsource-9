from __future__ import print_function
import unittest
from time import ctime, gmtime
import jdcal

from heatsource9.Dieties.ChronosDiety import Chronos

from heatsource9.Stream.PyHeatsource import CalcSolarPosition, GetStreamGeometry, CalcMuskingum, CalcFlows, \
    CalcHeatFluxes, GetSolarFlux, GetGroundFluxes, CalcMacCormick

# -*- coding: utf-8 -*-
"""Not implemented with Cython yet. Useful for testing individual functions within vanilla python"""

def CalcJulianCentury(start):
    # Then break out the time into a tuple
    y, m, d, H, M, S, day, wk, tz = gmtime(start)

    if m < 3:
        m += 12
        y -= 1

    julian_day = int(365.25 * (y + 4716.0)) + int(30.6001 * (m + 1)) + d - 1524.5

    # This value should only be added if we fall after a certain date
    if julian_day > 2299160.0:
        a = int(y / 100)
        b = (2 - a + int(a / 4))
        julian_day += b

    z = jdcal.gcal2jd(year=y, month=m, day=d)
    z1 = z[0] + z[1]
    if julian_day != z1:
        print(julian_day, z)
    

    # This is the julian century
    jdc = round((julian_day - 2451545.0) / 36525.0, 10)  # Eqn. 2-5 in HS Manual

    return jdc

# start=993945600
# stop=994550400
Chronos.Start(start=993945600, dt=60.0, stop=993945600 + (86400 * 1), offset=-7)

year, month, day, hour, minute, second, JD, offset, JDC = Chronos.TimeTuple()

jdcl = []
while Chronos.TheTime <= Chronos.stop:
    jdc = CalcJulianCentury(start=Chronos.TheTime)
    jdcl.append(jdc)
    Chronos(tick=True)




test_params = {
    "CalcSolarPosition": {
        "Inputs": [45.45428641, -121.6369944, 1, 8, 48, -7, 0.1732648871, True, 7],
        "Outputs": (-29.750374435040598, 119.7503744350406, 0, 0, 1.3897209316489807)
    },
    "GetStreamGeometry": {
        "Inputs": [1.922934707, 1.4, 3.0, 0.05, 0.054437256, 0.3921939243235582, 100, 12.0],
   	    "Outputs": (0.3921939243235582, 1.0105197168819202, 3.880452170684312, 0.2604128777867958, 3.7531635459413493, 1.902916563502042, 3.1276252722763966)
    },
    "CalcMuskingum": {
        "Inputs": [1.922934707000001, 1.5910330956534644, 4.210144453427711, 0.034807739000000004, 100, 12.0],
   	    "Outputs": (-0.4623191417424156, 0.9276387719263662, 0.5346803698160494)
    },
    "CalcFlows": {
        "Inputs": [1.875586564675247, 3.730393188777767, 1.27, 0.051572266000000005, 100, 12.0, 3.0, 0.05, 0.0, 1.9229347070000018, 1.9229347070000018, 1.922934707000002, 0.0, -1],
        "Outputs": (1.922934707000002, (0.4100655314629612, 1.0252444452399632, 3.863482138700792, 0.26536797853159777, 3.7303931887777675, 1.8755865646752472, 2.884530178274525))
    },
    "GetSolarFlux": {
        "Inputs": [6, 120, 4.481946711096697, 85.5180532889033, 1.0, 0.41895662744047685, 0.9500000000000001, 892.552, 0.4051860611296296, 0.8074010759147933, 0.9, 50, 'CanopyClosure', 0.2, False, [[0.5, [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]], [[0.0, [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [0.0, 0.0, 0.0396255, 0.205755, 0.1752825, 0.1752825, 0.231651, 0.2270745, 0.566961, 0.644649, 0.5471295, 0.603498, 0.681262, 0.504455, 0.291108, 0.3855765, 0.166092, 0.329133, 0.444996, 0.8930805, 1.203945, 0.9830095000000001, 0.6096, 0.534888, 0.7117335, 0.7498335, 0.6553275000000001, 0.7162725, 0.6370215, 0.7422059999999999, 0.5882430000000001, 0.5730255, 0.682749, 0.644612, 0.3017115, 0.27429000000000003, 0.6735960000000001, 0.437406, 0.34290000000000004, 0.5974335, 0.2392785, 0.0975196, 0.359643, 0.32001749999999995, 0.35049050000000004, 0.3230685, 0.4907235, 0.6431235, 0.4480095, 0.31395300000000004], [0.0, 0.3611685, 0.3672705, 0.47241749999999993, 0.4236765, 0.6964785, 0.653802, 0.2651745, 0.44347045, 0.545604, 0.4815705, 0.43740599999999996, 0.5440785, 0.09908244999999999, 0.2865315, 0.4099475, 0.3078885, 0.46787850000000003, 0.3246315, 0.2026665, 0.362694, 0.307851, 0.26059805, 0.09904494999999999, 0.2133825, 0.4053705, 1.1978425, 1.0774805, 0.409947, 0.2773785, 0.530349, 0.40689600000000004, 0.31399, 0.451098, 0.3139155, 0.2453805, 0.323106, 0.385614, 0.35048999999999997, 0.650751, 0.676647, 0.728437, 0.7726775, 0.3672705, 0.368796, 0.48309599999999997, 0.6873255, 0.583704, 0.082302, 0.33225899999999997], [0.0, 0.0, 0.02894705, 0.37642349999999997, 0.31704150000000003, 0.435843, 1.120115, 0.4556745, 0.7086840000000001, 0.260598, 0.32001749999999995, 0.742167, 0.69949, 0.2621235, 0.8655845, 0.7863705, 0.42672750000000004, 0.4876725, 0.333747, 0.5516685, 0.5699745, 0.6156655, 0.44957244999999996, 0.710208, 0.6400725, 0.966156, 0.6888885, 0.6812235, 0.598959, 0.207243, 0.6126152500000001, 0.5821785, 1.0256485, 0.2971725, 0.099045, 0.03047255, 0.1082355, 0.082302, 0.059457, 0.0594195, 0.393204, 0.2453805, 0.065559, 0.38859, 0.545604, 0.6721079999999999, 0.5806155, 0.469404, 0.4251645, 0.374898], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2133825, 0.281955, 0.095994, 0.1264665, 0.542515, 0.1097235, 0.1813845, 0.231651, 0.53035, 0.1127745, 0.1127745, 1.00433, 0.929655, 0.905245, 0.399306, 0.0, 0.0, 0.0960315, 0.0762, 0.3032745, 0.432792, 0.134094, 0.086841, 0.2667, 0.208806, 0.272802, 0.454149, 0.349002, 0.486147, 0.4556745, 0.07467444999999999, 0.2133075, 0.143247, 0.516657, 0.705594, 0.528861, 0.379512, 0.3429, 0.32917050000000003, 0.2469435, 0.35048999999999997, 0.3611685], [0.0, 0.0, 0.995175, 1.3578700000000001, 1.0302245, 0.8793145, 1.0942595, 1.281746, 1.0652760000000001, 0.504379, 0.46932949999999996, 0.498351, 0.3992685, 0.379437, 0.2240235, 0.17833349999999998, 0.8184045, 0.402357, 0.5928195, 0.43126675000000003, 0.37486074999999996, 0.4937745, 0.486147, 0.300186, 0.548655, 0.37493550000000003, 0.6126510000000001, 0.492249, 0.137145, 0.19812749999999998, 0.1859235, 0.167655, 0.22856254999999998, 0.20728055, 0.39167850000000004, 0.37489805000000004, 0.2682625, 0.198127, 0.2224605, 0.2072805, 0.295647, 0.30632550000000003, 0.158502, 0.1889745, 0.33527300000000004, 0.28496900000000003, 0.16307850000000002, 0.167655, 0.178296, 0.175245], [0.0, 1.1872, 1.1429985, 0.7223744999999999, 0.5851919999999999, 0.441945, 0.19809, 0.213345, 0.2880195, 0.1523999, 0.3261195, 0.22249799999999997, 0.108198, 0.11735100000000001, 0.219447, 0.2270745, 0.22860000000000003, 0.1493865, 0.356592, 0.5318745, 0.12955505, 0.20880605, 0.3215805, 0.1905, 0.1813845, 0.3108645, 0.4998765, 0.2849684, 0.249957, 0.46784100000000006, 0.443508, 0.143247, 0.08992939999999999, 0.060945150000000003, 0.129555, 0.1508745, 0.08844135, 0.0899295, 0.13413150000000001, 0.13714500000000002, 0.185886, 0.1859235, 0.11430000000000001, 0.13714500000000002, 0.155451, 0.317004, 0.371847, 0.416049, 0.405408, 0.358155], [0.0, 0.0, 1.210045, 2.234207, 0.8138285, 0.324594, 0.18134699999999998, 0.496863, 0.227112, 0.36273150000000004, 0.2453805, 0.18744905, 0.18134699999999998, 0.27127650000000003, 0.08535290000000001, 0.2590725, 0.361206, 0.629394, 1.435597, 0.365745, 0.153888, 0.355104, 0.149349, 0.17833345, 0.10510975, 0.18134699999999998, 0.39015299999999997, 0.29721, 0.24843149999999997, 0.248394, 0.288057, 0.46028800000000003, 0.25140799999999996, 0.16307850000000002, 0.15083725, 0.172194, 0.1036214, 0.1005707, 0.117351, 0.07768825, 0.143247, 0.15239999999999998, 0.1950395, 0.10671, 0.0625078, 0.24991945000000002, 0.5150939999999999, 0.8701964999999999, 1.866862, 2.3332525]], [[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]], (17.99435805205646, 33.439324015, 11.080199224355127, (1.0503049618998386, 17.344410947168104, 16.52914314427812, 17.062377251348227, 16.16248680763239, 17.99435805205646, 15.813317502416824, 10.363252774775665, 10.426290537923872, 10.327894695507561, 9.80024486343001, 8.79211261835742, 8.868485542023645, 5.994463783972589, 6.45349285897391, 7.058200741455669, 6.750052314409134, 7.333439380603994, 6.881189930477238, 6.610979108393911, 7.042003693514501, 6.5769060394903835, 6.114794558215523, 5.413786099816994, 5.532492834838794, 5.831468237902988, 7.30798154900395, 6.7530582703274105, 5.0119663831001215, 4.35114266896971, 4.742938618135295, 4.1078899350544305, 3.5229864374886084, 3.707057068591491, 3.3165639360854544, 3.169041652591424, 3.2974963891436877, 3.3236339540626214, 3.1733044622464934, 3.3793138413187553, 3.219528949193302, 3.0996405719732953, 3.16016632617885, 2.681639214982039, 2.639108112486511, 2.5822290331139426, 2.646624242903604, 2.424608817039321, 1.870610043412981, 0.5140681307300208)), 2, True],
        "Outputs": ([105.3248916947013, 5.3352037652941044, 3.1441634525872972, 2.538600954470955, 2.538600954470955, 2.310126868568569, 2.192488898891188, 0.11430166893371396], [0, 5.285961284899402, 3.1441634525872972, 2.538600954470955, 2.538600954470955, 2.310126868568569, 2.192488898891188, 0.11430166893371396], [105.3248916947013, 0.049242480394702096, 0, 0, 0, 0.0, 0.0, 0.0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6055624981163423])
    },
    "GetGroundFluxes": {
        "Inputs": [0.6612, 1.70501056, 0.99928, 7.33490555536, 904.4114999999999, 0.2, [[0.0, [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [0.0, 0.0, 0.0, 0.0, 0.0, 0.1539255, 0.1539255, 0.231651, 0.0381, 0.0381, 0.0746745, 0.0990825, 0.0990825, 0.0381, 0.0685725, 0.085353, 0.04267645, 0.1539255, 0.067047, 0.067047, 0.063996, 0.1447725, 0.14481, 0.1707435, 0.463302, 0.5715, 0.373335, 0.393204, 0.6522764999999999, 0.568449, 0.5653980000000001, 0.4587255, 0.2118195, 0.34900200000000003, 8.0695735, 10.3890735, 10.485105, 11.271557, 9.131854, 6.993624499999999, 7.3563825, 0.3368355, 0.317004, 0.2118195, 0.254496, 0.2514825, 0.2362275, 0.27123905, 0.431304, 0.34900200000000003], [0.0, 0.0, 0.5440785, 0.45113549999999997, 0.49987649999999995, 0.481608, 0.376386, 0.6141775, 0.406896, 0.214908, 0.17070605, 0.11277445, 0.07772535, 0.2240234, 0.23466465, 0.2286001, 0.129555, 0.19050005, 0.193551, 0.16307844999999999, 0.1371451, 0.24843149999999997, 0.134169, 0.2316135, 0.217959, 0.50445295, 0.6187155, 0.4480845, 0.374898, 0.23619, 0.510555, 0.4084215, 0.2560215, 0.34747649999999997, 0.5958705, 0.48771000000000003, 0.48923550000000005, 2.078683, 3.4549355, 3.89688, 3.2613469999999998, 4.0782251, 4.4028585, 4.5308495, 4.896631, 6.188944, 17.0216, 15.390845, 15.273499999999999, 15.575275], [0.0, 0.0, 0.102096, 0.38553899999999997, 0.20117849999999998, 0.1524375, 0.24534299999999998, 0.259035, 0.2971725, 0.3352725, 0.416049, 0.196602, 0.08077645, 0.1036217, 0.2286375, 0.2880195, 0.37489799999999995, 0.483096, 0.408459, 0.23165105, 0.387102, 0.19812755, 0.158502, 0.17680795, 0.2300882, 0.26975105, 0.26822555000000003, 0.1828725, 0.2514825, 0.0381, 0.1143, 0.050304, 0.0396255, 0.0396255, 0.0594195, 0.17375695, 0.1737195, 0.21795899999999999, 0.566961, 0.5547570000000001, 0.3154785, 0.23321385, 0.20270400000000002, 0.11277445, 0.2453805, 0.1538881, 4.753349500000001, 11.4681, 9.03427645, 7.47062645], [0.0, 0.0, 0.0, 0.0594195, 0.126504, 0.091455, 0.0746745, 0.04420195, 0.10671, 0.2849685, 0.1737195, 0.12189, 0.298698, 0.225549, 0.804675, 0.7071555, 0.755898, 0.8382015, 0.821457, 0.5608215, 0.5440784999999999, 0.45723749999999996, 0.355104, 0.161553, 0.10514699999999999, 0.09450605, 0.10209605, 0.143247, 0.129555, 0.175245, 0.272802, 0.4023195, 0.301749, 0.374898, 0.41757449999999996, 0.2179215, 0.073149, 0.0807765, 0.0259333, 0.01674315, 0.03356075, 0.10972345, 0.15239999999999998, 0.12951775, 0.14934895, 0.2423295, 0.45567450000000004, 0.624855, 0.5532315, 0.31090205], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0365745, 0.0381, 0.060945, 0.035049, 0.0518295, 0.0518295, 0.0396255, 0.0365745, 0.0365745, 0.0624705, 0.0777255, 0.193551, 0.18592350000000002, 0.384051, 0.193551, 0.19965300000000002, 0.24694349999999998, 0.24995699999999998, 0.2743275, 0.6202785, 0.947922, 0.8838885000000001, 0.31242749999999997, 0.14782355, 0.1371825, 0.17982150000000002, 0.178296, 0.172194, 0.2179215, 0.1767705, 0.15697650000000002, 0.3139905, 0.222498, 0.2743275, 0.2164335, 0.376386, 0.3154785, 0.29412150000000004, 0.1798215, 0.127992, 8.0878705, 8.1092275, 8.5344225, 5.90700295, 5.97405], [0.0, 0.0, 0.234702, 0.0746745, 0.22402350000000001, 0.181347, 0.225549, 0.1752075, 0.222498, 0.310902, 0.6080745, 0.580653, 0.4724175, 0.428253, 0.330696, 0.3764235, 0.2880195, 0.20114100000000001, 0.2682255, 0.251445, 0.15697650000000002, 0.6110880000000001, 0.5760765000000001, 0.48919799999999997, 0.534888, 0.13108055000000002, 0.0533549, 0.16307844999999999, 0.08840395000000001, 0.3688335, 0.34598795, 0.07467455, 0.3185295, 0.414561, 3.3177885000000003, 3.198873, 3.2674465, 3.776476, 4.4790555, 4.44553245, 7.7601755, 6.7574255, 7.03325, 6.318474500000001, 3.1668745, 4.302249, 0.89613, 1.037855, 0.81837, 0.095994], [0.0, 0.0, 0.2362275, 0.4953, 0.559296, 0.7620015, 0.827523, 0.9402595, 0.557733, 0.135657, 0.0960315, 0.09911974999999999, 0.09900775, 0.1524, 0.134094, 0.2148705, 0.4922115, 0.4084215, 0.358155, 0.371847, 0.2179215, 0.42825295, 0.22558650000000002, 0.2270745, 0.3916785, 0.361206, 0.41151000000000004, 0.44961, 0.35205299999999995, 0.431304, 0.294159, 0.4114725, 0.352053, 0.518145, 0.5852295, 0.2666625, 0.3505275, 0.2072804, 0.16151595, 0.08687845, 0.10514699999999999, 0.09599415, 0.0747119, 0.164604, 0.412998, 0.547092, 0.6263805, 0.6050610000000001, 0.5989225, 0.09599425]], 0.860723391598222, 0.1, 100, 12.0, 1.57, 0.0077, True, 18.0, 3.8500990115744935, 3.717440256087613, False, False, 1.51e-09, 1.6e-09, False, 5.279040571499248, 5.780844610467854, 0.03845869414, 0, 0],
   	    "Outputs": (15.756646823614231, 5.78970564195149, -36.779421391058, 245.50300709917593, -327.35904723993093, 45.076618749697, -0.06824567705006168, 12.223849244818796, 0)
    },
    "CalcMacCormick": {
        "Inputs": [12.0, 100, 1.8349000098530188, 6.238583245714886, 5.436950908428746, 0.03845869413999999, (), (), 1.9229347069999994, 2.9716933523650883e-05, 3.9478137283539043, 0, 0.0, 5.441134354577573, 5.436950908428746, 5.432185302806111, 0.0, 0.0, 0.01673441485270377],
   	    "Outputs": (5.441336724934847, 0.0003654847088417174, 0.015636252767397885)
    },
    "CalcHeatFluxes": {
        "Inputs": [(0.6607333333333334, 1.7321309866666668, 0.9992683333333333, 7.304209259053333), (1.27, 792.9845, 0.536682307574074, 0.49081853433290834, 0.2,
            [[0.5, [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]],
            [[0.0, [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]],
            [0.0, 0.0, 0.0, 12.2834245, 12.528805, 6.243845, 1.655042, 0.3962175, 0.583704, 0.611088, 0.7071195, 0.506016, 0.539502, 0.539502, 6.5135749999999994, 5.128245, 6.9235500000000005, 6.4876715, 5.5915235, 5.9496835, 5.667691, 5.614368499999999, 5.074889, 5.03984, 1.0713765, 1.0759505, 4.407395, 4.4317656, 3.7383755, 0.57908925, 0.58065195, 0.5334, 1.1323215, 1.3899059999999999, 1.2359445, 0.6111255, 0.6111255, 0.461739, 0.33527250000000003, 0.6918645, 0.6979665, 7.87295, 7.96443, 8.21593, 8.81946, 8.795, 8.48105, 8.578605, 6.1706175, 5.856739999999999], [0.0, 0.0, 13.9658951, 11.7973295, 1.487424, 1.5697285, 8.423178499999999, 7.517902, 7.380756, 6.7376275, 2.627373, 2.1930945, 0.26513699999999996, 0.8364875, 0.8410295, 5.3842795, 9.0967245, 10.8371716, 24.0213, 26.295099999999998, 26.37885, 25.664250000000003, 24.9159, 25.72505, 25.69165, 25.304499999999997, 24.1524, 23.6144, 16.410425, 19.8596, 10.482206, 6.576097, 6.862558, 8.042152, 10.011204000000001, 9.838976500000001, 9.9624, 8.706599, 6.5136295, 6.146249, 16.349475, 13.3395755, 14.40945, 21.38625, 21.52955, 21.7932, 18.91285, 14.97325, 13.87755, 7.955309000000001], [0.0, 0.0, 0.79705, 23.175449999999998, 26.85745, 12.899152, 12.8747285, 11.870455, 12.415995, 12.259054, 10.9316695, 8.055902, 8.8407265, 0.31395300000000004, 0.9052475, 0.6049849999999999, 0.5760765, 0.5334, 0.6614275000000001, 1.998648, 3.5870189999999997, 2.34393, 2.2814595, 0.9220275, 9.479248, 1.566676, 10.628396, 12.3932, 9.732308, 12.448045, 6.467901, 8.7294765, 7.7998265, 7.796805, 4.872223, 9.848051, 10.4576715, 9.8129655, 12.704046, 12.414502, 8.860533499999999, 8.3164205, 6.4053705, 1.1247315, 0.289508, 0.254459, 0.2651745, 0.2103315, 0.2971725, 5.8689285], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1157885, 0.123453, 15.02965, 14.87885295, 14.7964895, 15.336009, 15.529606000000001, 14.8833745, 14.778255999999999, 14.4338295, 13.078964000000001, 15.471653, 13.805909, 12.876299000000001, 12.541058, 12.245295, 13.83182, 13.926297, 13.581929500000001, 16.495794, 15.793254000000001, 14.9991755, 18.041128500000003, 17.923805, 17.763749, 15.669751, 10.413519500000001, 8.438371499999999, 7.2130715, 6.4129795000000005, 0.548655, 0.470892, 0.4358805, 0.3657825, 0.33225899999999997, 0.3779865, 0.504416, 0.57909, 0.420663, 0.530349, 1.2466195, 1.5133195000000002, 1.6825],
            [0.0, 0.0, 0.0, 17.7195675, 16.2489225, 16.264177500000002, 14.14275, 13.1262255, 11.210552999999999, 11.210552999999999, 9.1318305, 8.5679, 8.5679, 7.7297, 12.4069, 12.4069, 10.9911, 11.69515, 11.69515, 11.4544, 10.84635, 9.9883, 9.9883, 7.30145, 3.797795, 3.797795, 0.0762, 16.920955, 16.995655, 17.13587, 17.907030000000002, 15.5615775, 13.2161775, 15.494439999999999, 18.02435, 17.5458, 9.930354999999999, 6.748272500000001, 10.96063, 4.892018, 6.627905, 6.047215, 7.3913649999999995, 7.6900699999999995, 7.365445, 6.7893685, 7.027159999999999, 7.07895, 7.07895, 7.4341], [0.0, 0.0, 18.0411275, 17.486399000000002, 16.989609, 14.2356675, 13.392898, 13.603200000000001, 12.214845, 8.724896, 9.69714, 3.19125, 3.921245, 3.8816235, 2.249425, 1.0789645, 7.0241845000000005, 7.4751735, 11.477228499999999, 12.141753, 12.524246, 14.503929999999999, 15.2933725, 20.75085, 19.8227, 19.20245, 18.2941, 20.094, 20.1991, 7.9796795000000005, 7.923294, 8.831593, 7.187209999999999, 8.621256, 8.542057, 8.473454, 6.998193, 7.016502, 6.3383255, 5.6098705, 1.17805, 5.0688260000000005, 5.1770605, 5.018522999999999, 4.989574, 6.246899, 6.33225, 6.740647, 6.626347, 10.137703], [0.0, 0.0, 0.1569765, 16.419572499999997, 16.5460805, 16.300697, 16.296128500000002, 16.9408305, 15.558559, 13.55137, 13.293875, 11.5366745, 12.862545, 13.085045000000001, 12.797026500000001, 11.4040825, 9.5570165, 9.6849735, 9.6439, 3.2400255, 2.7157795, 0.1539255, 7.831844, 2.514564, 14.9534815, 3.4747255, 12.80312645, 28.5689, 28.40125, 18.39015, 11.9146, 12.990549999999999, 9.9014795, 17.60375, 19.17645, 11.474223499999999, 11.4925295, 11.838478499999999, 11.6860195, 10.971295999999999, 10.696971499999998, 9.0296765, 7.7830675000000005, 7.9537265, 9.7871155, 9.8008715, 9.8039225, 8.1838195, 3.7657985, 0.31692925]],
            [[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]],
            0.1, 100, 12.0, 1.57, 0.0077, 0.0, 0.0, True, 0.9, 50, 'CanopyClosure', False, 1.51e-09, 1.6e-09, False, False, True, 18.0), 0.4100655314629611, 1.0252444452399627, 3.863482138700791, 3.7303931887777666, 1.8755865646752468, (), (), 5.256842593474594, 5.628917350311523, 0.03845869414000002, 5.257592773398523, (77.79709448995658, 58.838719295000004, 8.281560289616591, (8.281560289616591, 4.8268587811207615, 5.930624588653834, 77.79709448995658, 75.08174174180614, 72.05475965233194, 69.69125605986696, 67.94986876766909, 63.499256914231594, 58.014044607486774, 55.15497508708504, 48.90894421068062, 49.55798228609745, 47.7623864833772, 45.234639374580716, 40.436258884984895, 34.243903050471246, 32.77196813031111, 31.28883631661687, 12.512200806478454, 10.711963504735982, 3.6424115706783504, 23.393364922314444, 9.862053647136422, 35.78235640665888, 11.332828000807718, 30.006215333940023, 49.815839199089304, 48.67200780872913, 36.12272948468731, 25.6094522432974, 26.997183946887038, 21.201859127975833, 32.08105861993237, 33.27244051516589, 21.778117094429643, 21.15857665291904, 21.23009812419643, 20.392752840819384, 18.924557339999698, 18.036416695957232, 15.212906263201116, 13.094796934135422, 12.935210322275148, 15.143345975415277, 14.7974381217105, 14.480825772450086, 12.049323066104847, 6.0420193998384315, -86.7487408223357)), 6, 2.8845301782745234, 0, 120, 0, -28.275348265426487, 118.27534826542649, 1.9229347070000005, 5.256116331302355, False, 0.0058322000590811385, True],
   	    "Outputs": ([0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], (11.683147364679588, 5.641639044658342, -22.654273522536897, 139.87687834357652, -327.25468261546473, 164.7235307493513, -0.06995222382339764, 12.455313806586075, 0), 1.4142354249053675, 1.4792056198925086e-05, (5.258401353930547, 0.00012989670466281646, 0.007559268889332671))
    }
}

def test_calc_flows():
    assert CalcFlows(*test_params["CalcFlows"]["Inputs"]) == test_params["CalcFlows"]["Outputs"]

def test_calc_muskingum():
    assert CalcMuskingum(*test_params["CalcMuskingum"]["Inputs"]) == test_params["CalcMuskingum"]["Outputs"]

def test_get_stream_geometry():
    assert GetStreamGeometry(*test_params["GetStreamGeometry"]["Inputs"]) == test_params["GetStreamGeometry"]["Outputs"]

def test_calc_solar_position():
    assert CalcSolarPosition(*test_params["CalcSolarPosition"]["Inputs"]) == test_params["CalcSolarPosition"]["Outputs"]

def test_get_solar_flux():
    assert GetSolarFlux(*test_params["GetSolarFlux"]["Inputs"]) == test_params["GetSolarFlux"]["Outputs"]

def test_get_ground_fluxes():
    assert GetGroundFluxes(*test_params["GetGroundFluxes"]["Inputs"]) == test_params["GetGroundFluxes"]["Outputs"]

def test_calc_maccormick():
    assert CalcMacCormick(*test_params["CalcMacCormick"]["Inputs"]) == test_params["CalcMacCormick"]["Outputs"]

def test_calc_heat_fluxes():
    assert CalcHeatFluxes(*test_params["CalcHeatFluxes"]["Inputs"]) == test_params["CalcHeatFluxes"]["Outputs"]
