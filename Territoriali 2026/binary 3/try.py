import angr
proj = angr.Project("./../supersecurebank",
    load_options={"auto_load_libs":False},
    main_opts={"base_addr":0,"force_rebase":True}
)
init = proj.factory.entry_state()
sim = proj.factory.simulation_manager(init)
s = sim.explore(find=0x40077D,avoid=[0x40076C,0x4005D1]) #quelli che trova stanno in found
print(s.found[0].posix.dumps(0).decode())#281!!! posix è tipo buffer di input tipo input