import omni.ext
import omni.ui as ui


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[spawn.cube] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class SpawnCubeExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[spawn.cube] spawn cube startup")

        self._count = 0

        self._window = ui.Window("Spawn a cube", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("Cube Spawner")


                def on_click():
                    omni.kit.commands.execute("CreatePrimWithDefaultXform", prim_type="Cube", attributes={'size:':100, 'extent': [(-50,-50,-50), (50,50,50)]})
                    print("Cube spawned!")

                def on_reset():
                    self._count = 0
                    label.text = "empty"

                on_reset()

                with ui.HStack():
                    ui.Button("Spawn Cube", clicked_fn=on_click)
                    #ui.Button("Reset", clicked_fn=on_reset)

    def on_shutdown(self):
        print("[spawn.cube] spawn cube shutdown")
