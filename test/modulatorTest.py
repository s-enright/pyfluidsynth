import unittest

import soundFontDefinitions.definitions as d

import fluidsynth


def local_file_path(file_name: str) -> str:
    """
    Return a file path to a file that is in the same directory as this file.
    """
    from os.path import dirname, join

    return join(dirname(__file__), file_name)


class TestModulatorMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fs = fluidsynth.Synth()
        cls.modulator = fluidsynth.Modulator()

        ## Your installation of FluidSynth may require a different driver.
        ## Use something like:
        # fs.start(driver="pulseaudio")
        cls.fs.start()
        cls.sfid = cls.fs.sfload(local_file_path("example.sf2"))
        cls.fs.program_select(0, cls.sfid, 0, 0)

    @classmethod
    def tearDownClass(cls):
        cls.fs.delete()

    def test_dest(self):
        assert self.modulator.has_dest(5) == None
        self.modulator.set_dest(5)
        assert self.modulator.has_dest(5) == True
        assert self.modulator.get_dest() == 5

    def test_flags(self):
        assert self.modulator.get_source1() == None
        self.modulator.set_source1(d.FLUID_MOD_KEY, 9)
        assert self.modulator.get_source1() == d.FLUID_MOD_KEY
        assert self.modulator.get_flags1() == 9

        assert self.modulator.get_source2() == None
        self.modulator.set_source2(d.FLUID_MOD_VELOCITY, 4)
        assert self.modulator.get_source2() == d.FLUID_MOD_VELOCITY
        assert self.modulator.get_flags2() == 4

    def test_transforms(self):
        assert self.modulator.get_transform() == None
        self.modulator.set_transform(d.FLUID_MOD_TRANSFORM_ABS)
        assert self.modulator.get_transform() == d.FLUID_MOD_TRANSFORM_ABS


if __name__ == "__main__":
    unittest.main()
