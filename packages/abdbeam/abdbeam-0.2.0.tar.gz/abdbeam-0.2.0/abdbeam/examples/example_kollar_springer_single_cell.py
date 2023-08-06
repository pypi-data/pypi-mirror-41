import abdbeam as ab

sc = ab.Section()
# Create a materials dictionary:
mts = dict()
mts[1] = ab.Laminate()
mts[1].ply_materials[1] = ab.PlyMaterial(0.0001, 148e9, 9.65e9, 4.55e9,
                                         0.3)
mts[1].ply_materials[2] = ab.PlyMaterial(0.0002, 16.39e9, 16.39e9,
                                         38.19e9, 0.801)
mts[1].plies = [[0,1]]*10 + [[45,1]]*10
mts[1].symmetry = 'T'
# Create a points dictionary based on Y and Z point coordinates:
pts = dict()
pts[1] = ab.Point(-0.025, -0.035)
pts[2] = ab.Point(0.025, -0.035)
pts[3] = ab.Point(0.025, 0.035)
pts[4] = ab.Point(-0.025, 0.035)
# Create a segments dictionary referencing point and material ids:
sgs = dict()
sgs[1] = ab.Segment(1,2,1)
sgs[2] = ab.Segment(2,3,1)
sgs[3] = ab.Segment(3,4,1)
sgs[4] = ab.Segment(4,1,1)
# Point the dictionaries to the section
sc.materials = mts
sc.points = pts
sc.segments = sgs
# Calculate and output section properties
sc.calculate_properties()
sc.summary()
ab.plot_section(sc, segment_coord=True, figsize=(6.4*0.8, 4.8*0.8))
# Create a single load case and calculate its internal loads
sc.loads[1] = ab.Load(Px=200, Mz=10, Vz_s=-100)
sc.calculate_internal_loads()
# Plot internal loads
ab.plot_section_loads(sc, 1, int_load_list=['Nx', 'Nxy'],
                      title_list=['Abdbeam - Nx (N/m)',
                      'Abdbeam - Nxy (N/m)'], figsize=(6.4*0.8, 4.8*0.8))