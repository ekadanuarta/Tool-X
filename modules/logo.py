red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
purple="\033[1;35m"
cyan="\033[1;36m"
violate="\033[1;37m"
nc="\033[00m"

class logo:
  @classmethod
  def tool_header(self):
    print(f'''\007

{yellow}
         _____           _    __  __
        |_   _|__   ___ | |   \ \/ /
          | |/ _ \ / _ \| |____\  /
          | | (_) | (_) | |____/  \    
          |_|\___/ \___/|_|   /_/\_\ {purple}v2.1


{cyan} =============================================
{yellow}|          Install Best Hacking Tool          |
{cyan} ============================================={nc}''')

  @classmethod
  def tool_footer(self):
    print(f'''{cyan}_______________________________________________
==============================================={nc}''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print (f'''
{cyan}  [ + ]  {red}We can't install Tool-X.
{cyan}  [ + ]  {red}There are some error.
{cyan}  [ + ]  {red}Please try again after some time!''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print (f'''
{yellow}  [ + ] {green}Use It At Your Own Risk.
{yellow}  [ + ] {green}No Warranty.
{yellow}  [ + ] {green}Use it legal purpose only.
{yellow}  [ + ] {green}We are not responsible for your actions.
{yellow}  [ + ] {green}Do not do things that are forbidden.

{red} If you are installing this tool.
 that means you are agree with all terms.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print (f'''
{yellow}    [ + ] {green}Tool-X installed successfully.
{yellow}    [ + ] {green}To run Tool-X,
{yellow}    [ + ] {green}Type Tool-X in your terminal.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print (f'''
{yellow}  [ 1 ] {green}Update your Tool-X.
{yellow}  [ 0 ] {green}For Back.{nc}''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print (f'''
{yellow}      [ + ] {green}Tool-X Updated Successfully.
{yellow}      [ + ] {green}Press Enter to continue.{nc}''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print (f'''
{cyan}  [ + ]  {red}No network connection?
{cyan}  [ + ]  {red}Are you offline?
{cyan}  [ + ]  {red}Please try again after some time.{nc}''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print (f'''
{red}  [ + ]  {red}We can't Update Tool-X.\033[1;m
{red}  [ + ]  {red}Please try again after some time.{nc}''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
{yellow}       [+] Tool Name :- {green}Tool-X
{yellow}       [+] Latest Update :- {green}23/3/2019.\033[1;m
{yellow}       [+] Tools :- {green}total {total} tools.\033[1;m

{yellow} [+] {green}Tool-x is automatic tool installer.
{yellow} [+] {green}Made for termux and linux based system.
{red} [+] Note :- Use this tool at your own risk.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print (f"""{yellow} =============================================
{green}|_____________ Select your tool ______________|
 {yellow}============================================={nc}""")

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
{yellow}  [ + ] {green}Sorry ??
{yellow}  [ + ] {violate}'{name}'{green} is already Installed !!
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
{yellow}  [ + ] {green}Installed Successfully !!
{yellow}  [ + ] {violate}'{name}'{green} is Installed Successfully !!
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
{yellow}  [ + ] {red}Sorry ??
{yellow}  [ + ] {violate}'{name}'{red} is not installed !!
''')
    self.tool_footer()

  @classmethod
  def back(self):
    print (f"""\033[01;36m =============================================
{yellow}|  00) Back                                   |
 \033[01;36m============================================={nc}""")

  @classmethod
  def updating(self):
    print (f"""{yellow} =============================================
{green}|______________ Updating Tool-X ______________|
 {yellow}============================================={nc}""")

  @classmethod
  def installing(self):
    print (f"""{yellow} =============================================
{green}|________________ Installing _________________|
 {yellow}============================================={nc}""")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
{yellow}  [ 1 ] {green}Show all tools.{yellow} [ {purple}{total} tools{yellow} ]
{yellow}  [ 2 ] {green}Tools Category.
{yellow}  [ 3 ] {green}Update Tool-X.
{yellow}  [ 4 ] {green}About Us.
{yellow}  [ x ] {green}For Exit.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print (f'''
{yellow}         [ + ] {green}Thanks for using Tool-X
{yellow}         [ + ] {green}Good Bye.....! ){nc}''')
    self.tool_footer()
