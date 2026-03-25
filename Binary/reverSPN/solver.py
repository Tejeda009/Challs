import angr
import claripy

proj = angr.Project(
    "./../reverSPN",
    auto_load_libs=False,
    main_opts={"base_addr": 0}
)
stdin = angr.SimFileStream(name='stdin', content=b'admin\x00\n', has_end=False) #this is in the case that you want to add something before the true input. in this case the first input needed to be cat flag.txt so i put that. to put the \n however you forefully need to do \x00 otherwise it won't work

# Create initial state with this stdin
state = proj.factory.full_init_state(stdin=stdin) #this in an alternative to entry_state() in case it doesn't work 
# silence uninitialized memory warnings
state.options.add(angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY)
state.options.add(angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS)


sim = proj.factory.simulation_manager(state)

sim.explore(find=0x1262, avoid=0x1270)
print(sim.found[0].posix.dumps(0))