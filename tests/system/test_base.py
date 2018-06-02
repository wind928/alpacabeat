from alpacabeat import BaseTest

import os


class Test(BaseTest):

    def test_base(self):
        """
        Basic test with exiting Alpacabeat normally
        """
        self.render_config_template(
            path=os.path.abspath(self.working_dir) + "/log/*"
        )

        alpacabeat_proc = self.start_beat()
        self.wait_until(lambda: self.log_contains("alpacabeat is running"))
        exit_code = alpacabeat_proc.kill_and_wait()
        assert exit_code == 0
