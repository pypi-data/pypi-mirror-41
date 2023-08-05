#@+leo-ver=5-thin
#@+node:ekr.20130925160837.11429: * @file leoConfig.py
'''Configuration classes for Leo.'''
# pylint: disable=unsubscriptable-object
#@+<< imports >>
#@+node:ekr.20041227063801: ** << imports >> (leoConfig)
import os
import sys
from leo.plugins.mod_scripting import build_rclick_tree
import leo.core.leoGlobals as g
#@-<< imports >>
#@+<< class ParserBaseClass >>
#@+node:ekr.20041119203941.2: ** << class ParserBaseClass >>
class ParserBaseClass(object):
    """The base class for settings parsers."""
    #@+<< ParserBaseClass data >>
    #@+node:ekr.20041121130043: *3* << ParserBaseClass data >>
    # These are the canonicalized names.
    # Case is ignored, as are '_' and '-' characters.
    basic_types = [
        # Headlines have the form @kind name = var
        'bool', 'color', 'directory', 'int', 'ints',
        'float', 'path', 'ratio', 'string', 'strings']
    control_types = [
        'buttons',
        'commands', 'data',
        'enabledplugins', 'font',
        'ifenv', 'ifhostname', 'ifplatform',
        'ignore',
        'menus', 'mode', 'menuat',
        'openwith', 'outlinedata',
        'popup',
        'settings', 'shortcuts',
        ]
    # Keys are settings names, values are (type,value) tuples.
    settingsDict = {}
    #@-<< ParserBaseClass data >>
    #@+others
    #@+node:ekr.20041119204700: *3*  ctor (ParserBaseClass)
    #@@nobeautify

    def __init__ (self,c,localFlag):
        '''Ctor for the ParserBaseClass class.'''
        self.c = c
        self.clipBoard = []
        self.localFlag = localFlag
            # True if this is the .leo file being opened,
            # as opposed to myLeoSettings.leo or leoSettings.leo.
        self.shortcutsDict = g.TypedDictOfLists(
            name='parser.shortcutsDict',
            keyType=type('shortcutName'),
            valType=g.BindingInfo)
        self.openWithList = []
            # A list of dicts containing 'name','shortcut','command' keys.
        # Keys are canonicalized names.
        self.dispatchDict = {
            'bool':         self.doBool,
            'buttons':      self.doButtons, # New in 4.4.4
            'color':        self.doColor,
            'commands':     self.doCommands, # New in 4.4.8.
            'data':         self.doData, # New in 4.4.6
            'directory':    self.doDirectory,
            'enabledplugins': self.doEnabledPlugins,
            'font':         self.doFont,
            'ifenv':        self.doIfEnv, # New in 5.2 b1.
            'ifhostname':   self.doIfHostname,
            'ifplatform':   self.doIfPlatform,
            'ignore':       self.doIgnore,
            'int':          self.doInt,
            'ints':         self.doInts,
            'float':        self.doFloat,
            'menus':        self.doMenus, # New in 4.4.4
            'menuat':       self.doMenuat,
            'popup':        self.doPopup, # New in 4.4.8
            'mode':         self.doMode, # New in 4.4b1.
            'openwith':     self.doOpenWith, # New in 4.4.3 b1.
            'outlinedata':  self.doOutlineData, # New in 4.11.1.
            'path':         self.doPath,
            'ratio':        self.doRatio,
            'shortcuts':    self.doShortcuts,
            'string':       self.doString,
            'strings':      self.doStrings,
        }
        self.debug_count = 0
    #@+node:ekr.20080514084054.4: *3* computeModeName (ParserBaseClass)
    def computeModeName(self, name):
        s = name.strip().lower()
        j = s.find(' ')
        if j > -1: s = s[: j]
        if s.endswith('mode'):
            s = s[: -4].strip()
        if s.endswith('-'):
            s = s[: -1]
        i = s.find('::')
        if i > -1:
            # The actual mode name is everything up to the "::"
            # The prompt is everything after the prompt.
            s = s[: i]
        modeName = s + '-mode'
        return modeName
    #@+node:ekr.20060102103625: *3* createModeCommand (ParserBaseClass)
    def createModeCommand(self, modeName, name, modeDict):
        modeName = 'enter-' + modeName.replace(' ', '-')
        i = name.find('::')
        if i > -1:
            # The prompt is everything after the '::'
            prompt = name[i + 2:].strip()
            modeDict['*command-prompt*'] = g.BindingInfo(kind=prompt)
        # Save the info for k.finishCreate and k.makeAllBindings.
        d = g.app.config.modeCommandsDict
        # New in 4.4.1 b2: silently allow redefinitions of modes.
        d[modeName] = modeDict
    #@+node:ekr.20041120103012: *3* error (ParserBaseClass)
    def error(self, s):
        g.pr(s)
        # Does not work at present because we are using a null Gui.
        g.blue(s)
    #@+node:ekr.20041120094940: *3* kind handlers (ParserBaseClass)
    #@+node:ekr.20041120094940.1: *4* doBool
    def doBool(self, p, kind, name, val):
        if val in ('True', 'true', '1'):
            self.set(p, kind, name, True)
        elif val in ('False', 'false', '0'):
            self.set(p, kind, name, False)
        else:
            self.valueError(p, kind, name, val)
    #@+node:ekr.20070925144337: *4* doButtons (ParserBaseClass)
    def doButtons(self, p, kind, name, val):
        '''Create buttons for each @button node in an @buttons tree.'''
        c, tag = self.c, '@button'
        aList, seen = [], []
        after = p.nodeAfterTree()
        while p and p != after:
            if p.v in seen:
                p.moveToNodeAfterTree()
            elif p.isAtIgnoreNode():
                seen.append(p.v)
                p.moveToNodeAfterTree()
            else:
                seen.append(p.v)
                if g.match_word(p.h, 0, tag):
                    # We can not assume that p will be valid when it is used.
                    script = g.getScript(c, p,
                        useSelectedText=False,
                        forcePythonSentinels=True,
                        useSentinels=True)
                    command_p = p.copy()
                    aList.append((command_p, script),)
                    rclicks = build_rclick_tree(command_p, top_level=True)
                    command_p.rclicks = rclicks
                p.moveToThreadNext()
        # This setting is handled differently from most other settings,
        # because the last setting must be retrieved before any commander exists.
        if aList:
            g.app.config.atCommonButtonsList.extend(aList)
                # Bug fix: 2011/11/24: Extend the list, don't replace it.
            g.app.config.buttonsFileName = c.shortFileName() if c else '<no settings file>'
        d, key = g.app.config.unitTestDict, 'config.doButtons-file-names'
        aList = d.get(key, [])
        aList.append(c.shortFileName())
        d[key] = aList
    #@+node:ekr.20041120094940.2: *4* doColor
    def doColor(self, p, kind, name, val):
        # At present no checking is done.
        val = val.lstrip('"').rstrip('"')
        val = val.lstrip("'").rstrip("'")
        self.set(p, kind, name, val)
    #@+node:ekr.20080312071248.6: *4* doCommands
    def doCommands(self, p, kind, name, val):
        '''Handle an @commands tree.'''
        aList = []; c = self.c; tag = '@command'
        seen = []
        after = p.nodeAfterTree()
        while p and p != after:
            if p.v in seen:
                p.moveToNodeAfterTree()
            elif p.isAtIgnoreNode():
                seen.append(p.v)
                p.moveToNodeAfterTree()
            else:
                seen.append(p.v)
                if g.match_word(p.h, 0, tag):
                    # We can not assume that p will be valid when it is used.
                    script = g.getScript(c, p,
                        useSelectedText=False,
                        forcePythonSentinels=True,
                        useSentinels=True)
                    aList.append((p.copy(), script),)
                p.moveToThreadNext()
        # This setting is handled differently from most other settings,
        # because the last setting must be retrieved before any commander exists.
        if aList:
            g.app.config.atCommonCommandsList.extend(aList)
                # Bug fix: 2011/11/24: Extend the list, don't replace it.
        d, key = g.app.config.unitTestDict, 'config.doCommands-file-names'
        aList = d.get(key, [])
        aList.append(c.shortFileName())
        d[key] = aList
    #@+node:ekr.20071214140900: *4* doData (ParserBaseClass)
    def doData(self, p, kind, name, val):
        # New in Leo 4.11: do not strip lines.
        # New in Leo 4.12.1: strip *nothing* here.
        # New in Leo 4.12.1: allow composition of nodes:
        # - Append all text in descendants in outline order.
        # - Ensure all fragments end with a newline.
        data = g.splitLines(p.b)
        for p2 in p.subtree():
            if p2.b and not p2.h.startswith('@'):
                data.extend(g.splitLines(p2.b))
                if not p2.b.endswith('\n'):
                    data.append('\n')
        self.set(p, kind, name, data)
    #@+node:ekr.20131114051702.16545: *4* doOutlineData & helper (ParserBaseClass)
    def doOutlineData(self, p, kind, name, val):
        # New in Leo 4.11: do not strip lines.
        data = self.getOutlineDataHelper(p)
        self.set(p, kind, name, data)
        return 'skip'
    #@+node:ekr.20131114051702.16546: *5* getOutlineDataHelper
    def getOutlineDataHelper(self, p):
        c = self.c
        if not p:
            return None
        try:
            # Copy the entire tree to s.
            c.fileCommands.leo_file_encoding = 'utf-8'
            s = c.fileCommands.putLeoOutline(p)
            s = g.toUnicode(s, encoding='utf-8')
        except Exception:
            g.es_exception()
            s = None
        return s
    #@+node:ekr.20041120094940.3: *4* doDirectory & doPath
    def doDirectory(self, p, kind, name, val):
        # At present no checking is done.
        self.set(p, kind, name, val)

    doPath = doDirectory
    #@+node:ekr.20070224075914: *4* doEnabledPlugins
    def doEnabledPlugins(self, p, kind, name, val):
        c = self.c
        s = p.b
        # This setting is handled differently from all other settings,
        # because the last setting must be retrieved before any commander exists.
        # 2011/09/04: Remove comments, comment lines and blank lines.
        aList, lines = [], g.splitLines(s)
        for s in lines:
            i = s.find('#')
            if i > -1: s = s[: i] + '\n' # 2011/09/29: must add newline back in.
            if s.strip(): aList.append(s.lstrip())
        s = ''.join(aList)
        # Set the global config ivars.
        g.app.config.enabledPluginsString = s
        g.app.config.enabledPluginsFileName = c.shortFileName() if c else '<no settings file>'
    #@+node:ekr.20041120094940.6: *4* doFloat
    def doFloat(self, p, kind, name, val):
        try:
            val = float(val)
            self.set(p, kind, name, val)
        except ValueError:
            self.valueError(p, kind, name, val)
    #@+node:ekr.20041120094940.4: *4* doFont
    def doFont(self, p, kind, name, val):
        '''Handle an @font node. Such nodes affect syntax coloring *only*.'''
        d = self.parseFont(p)
        # Set individual settings.
        for key in ('family', 'size', 'slant', 'weight'):
            data = d.get(key)
            if data is not None:
                name, val = data
                setKind = key
                self.set(p, setKind, name, val)
    #@+node:ekr.20150426034813.1: *4* doIfEnv
    def doIfEnv(self, p, kind, name, val):
        '''
        Support @ifenv in @settings trees.

        Enable descendant settings if the value of os.getenv is in any of the names.
        '''
        aList = name.split(',')
        if not aList:
            return 'skip'
        name = aList[0]
        env = os.getenv(name)
        env = env.lower().strip() if env else 'none'
        for s in aList[1:]:
            if s.lower().strip() == env:
                return None
        return 'skip'
    #@+node:dan.20080410121257.2: *4* doIfHostname
    def doIfHostname(self, p, kind, name, val):
        '''
        Support @ifhostname in @settings trees.

        Examples: Let h = os.environ('HOSTNAME')

        @ifhostname bob
            Enable descendant settings if h == 'bob'
        @ifhostname !harry
            Enable descendant settings if h != 'harry'
        '''
        lm = g.app.loadManager
        h = lm.computeMachineName().strip()
        s = name.strip()
        if s.startswith('!'):
            if h == s[1:]:
                return 'skip'
        elif h != s:
            return 'skip'
        else:
            return None
    #@+node:ekr.20041120104215: *4* doIfPlatform
    def doIfPlatform(self, p, kind, name, val):
        '''Support @ifplatform in @settings trees.'''
        platform = sys.platform.lower()
        for s in name.split(','):
            if platform == s.lower():
                return None
        return "skip"
    #@+node:ekr.20041120104215.1: *4* doIgnore
    def doIgnore(self, p, kind, name, val):
        return "skip"
    #@+node:ekr.20041120094940.5: *4* doInt
    def doInt(self, p, kind, name, val):
        try:
            val = int(val)
            self.set(p, kind, name, val)
        except ValueError:
            self.valueError(p, kind, name, val)
    #@+node:ekr.20041217132253: *4* doInts
    def doInts(self, p, kind, name, val):
        '''We expect either:
        @ints [val1,val2,...]aName=val
        @ints aName[val1,val2,...]=val'''
        name = name.strip() # The name indicates the valid values.
        i = name.find('[')
        j = name.find(']')
        if -1 < i < j:
            items = name[i + 1: j]
            items = items.split(',')
            name = name[: i] + name[j + 1:].strip()
            try:
                items = [int(item.strip()) for item in items]
            except ValueError:
                items = []
                self.valueError(p, 'ints[]', name, val)
                return
            kind = "ints[%s]" % (','.join([str(item) for item in items]))
            try:
                val = int(val)
            except ValueError:
                self.valueError(p, 'int', name, val)
                return
            if val not in items:
                self.error("%d is not in %s in %s" % (val, kind, name))
                return
            # At present no checking is done.
            self.set(p, kind, name, val)
    #@+node:tbrown.20080514112857.124: *4* doMenuat
    def doMenuat(self, p, kind, name, val):
        '''Handle @menuat setting.'''
        if g.app.config.menusList:
            # get the patch fragment
            patch = []
            if p.hasChildren():
                # self.doMenus(p.copy().firstChild(),kind,name,val,storeIn=patch)
                self.doItems(p.copy(), patch)
            # setup
            parts = name.split()
            if len(parts) != 3:
                parts.append('subtree')
            targetPath, mode, source = parts
            if not targetPath.startswith('/'):
                targetPath = '/' + targetPath
            ans = self.patchMenuTree(g.app.config.menusList, targetPath)
            if ans:
                # pylint: disable=unpacking-non-sequence
                list_, idx = ans
                if mode not in ('copy', 'cut'):
                    if source != 'clipboard':
                        use = patch # [0][1]
                    else:
                        if isinstance(self.clipBoard, list):
                            use = self.clipBoard
                        else:
                            use = [self.clipBoard]
                if mode == 'replace':
                    list_[idx] = use.pop(0)
                    while use:
                        idx += 1
                        list_.insert(idx, use.pop(0))
                elif mode == 'before':
                    while use:
                        list_.insert(idx, use.pop())
                elif mode == 'after':
                    while use:
                        list_.insert(idx + 1, use.pop())
                elif mode == 'cut':
                    self.clipBoard = list_[idx]
                    del list_[idx]
                elif mode == 'copy':
                    self.clipBoard = list_[idx]
                else: # append
                    list_.extend(use)
            else:
                g.es_print("ERROR: didn't find menu path " + targetPath)
        elif g.app.inBridge:
            pass # Not an error.
                # Fix: https://github.com/leo-editor/leo-editor/issues/48
        else:
            g.es_print("ERROR: @menuat found but no menu tree to patch")
    #@+node:tbrown.20080514180046.9: *5* getName (ParserBaseClass)
    def getName(self, val, val2=None):
        if val2 and val2.strip(): val = val2
        val = val.split('\n', 1)[0]
        for i in "*.-& \t\n":
            val = val.replace(i, '')
        return val.lower()
    #@+node:tbrown.20080514180046.2: *5* dumpMenuTree
    def dumpMenuTree(self, aList, level=0, path=''):
        for z in aList:
            kind, val, val2 = z
            if kind == '@item':
                name = self.getName(val, val2)
                g.es_print('%s %s (%s) [%s]' % ('    ' * (level + 0), val, val2, path + '/' + name))
            else:
                name = self.getName(kind.replace('@menu ', ''))
                g.es_print('%s %s... [%s]' % ('    ' * (level), kind, path + '/' + name))
                self.dumpMenuTree(val, level + 1, path=path + '/' + name)
    #@+node:tbrown.20080514180046.8: *5* patchMenuTree
    def patchMenuTree(self, orig, targetPath, path=''):

        for n, z in enumerate(orig):
            kind, val, val2 = z
            if kind == '@item':
                name = self.getName(val, val2)
                curPath = path + '/' + name
                if curPath == targetPath:
                    return orig, n
            else:
                name = self.getName(kind.replace('@menu ', ''))
                curPath = path + '/' + name
                if curPath == targetPath:
                    return orig, n
                ans = self.patchMenuTree(val, targetPath, path=path + '/' + name)
                if ans:
                    return ans
        return None
    #@+node:ekr.20070925144337.2: *4* doMenus & helper (ParserBaseClass)
    def doMenus(self, p, kind, name, val):

        c = self.c
        p = p.copy()
        aList = []
        after = p.nodeAfterTree()
        while p and p != after:
            self.debug_count += 1
            h = p.h
            if g.match_word(h, 0, '@menu'):
                name = h[len('@menu'):].strip()
                if name:
                    for z in aList:
                        name2, junk, junk = z
                        if name2 == name:
                            self.error('Replacing previous @menu %s' % (name))
                            break
                    aList2 = []
                    kind = '%s %s' % ('@menu', name)
                    self.doItems(p, aList2)
                    aList.append((kind, aList2, None),)
                    p.moveToNodeAfterTree()
                else:
                    p.moveToThreadNext()
            else:
                p.moveToThreadNext()
        if self.localFlag:
            self.set(p, kind='menus', name='menus', val=aList)
        else:
            g.app.config.menusList = aList
            name = c.shortFileName() if c else '<no settings file>'
            g.app.config.menusFileName = name
       
    #@+node:ekr.20070926141716: *5* doItems
    def doItems(self, p, aList):

        p = p.copy()
        after = p.nodeAfterTree()
        p.moveToThreadNext()
        while p and p != after:
            self.debug_count += 1
            h = p.h
            for tag in ('@menu', '@item', '@ifplatform'):
                if g.match_word(h, 0, tag):
                    itemName = h[len(tag):].strip()
                    if itemName:
                        lines = [z for z in g.splitLines(p.b) if
                            z.strip() and not z.strip().startswith('#')]
                        body = lines[0].strip() if lines else ''
                            # Only the first body line is significant.
                            # This allows following comment lines.
                        if tag == '@menu':
                            aList2 = []
                            kind = '%s %s' % (tag, itemName)
                            self.doItems(p, aList2)
                            aList.append((kind, aList2, body),)
                                # #848: Body was None.
                            p.moveToNodeAfterTree()
                            break
                        else:
                            kind = tag
                            head = itemName
                            aList.append((kind, head, body),)
                            p.moveToThreadNext()
                            break
            else:
                p.moveToThreadNext()
    #@+node:ekr.20060102103625.1: *4* doMode (ParserBaseClass)
    def doMode(self, p, kind, name, val):
        '''Parse an @mode node and create the enter-<name>-mode command.'''
        c = self.c
        name1 = name
        modeName = self.computeModeName(name)
        d = g.TypedDictOfLists(
            name='modeDict for %s' % (modeName),
            keyType=type('commandName'), valType=g.BindingInfo)
        s = p.b
        lines = g.splitLines(s)
        for line in lines:
            line = line.strip()
            if line and not g.match(line, 0, '#'):
                name, bi = self.parseShortcutLine('*mode-setting*', line)
                if not name:
                    # An entry command: put it in the special *entry-commands* key.
                    d.add('*entry-commands*', bi)
                elif bi is not None:
                    # A regular shortcut.
                    bi.pane = modeName
                    aList = d.get(name, [])
                    # Important: use previous bindings if possible.
                    key2, aList2 = c.config.getShortcut(name)
                    aList3 = [z for z in aList2 if z.pane != modeName]
                    if aList3:
                        aList.extend(aList3)
                    aList.append(bi)
                    d.replace(name, aList)
            # Restore the global shortcutsDict.
            # Create the command, but not any bindings to it.
            self.createModeCommand(modeName, name1, d)
    #@+node:ekr.20070411101643.1: *4* doOpenWith (ParserBaseClass)
    def doOpenWith(self, p, kind, name, val):

        d = self.parseOpenWith(p)
        d['name'] = name
        d['shortcut'] = val
        name = kind = 'openwithtable'
        self.openWithList.append(d)
        self.set(p, kind, name, self.openWithList)
    #@+node:bobjack.20080324141020.4: *4* doPopup & helper
    def doPopup(self, p, kind, name, val):
        """
        Handle @popup menu items in @settings trees.
        """
        popupName = name
        # popupType = val
        aList = []
        p = p.copy()
        self.doPopupItems(p, aList)
        if not hasattr(g.app.config, 'context_menus'):
            g.app.config.context_menus = {}
        g.app.config.context_menus[popupName] = aList
    #@+node:bobjack.20080324141020.5: *5* doPopupItems
    def doPopupItems(self, p, aList):
        p = p.copy(); after = p.nodeAfterTree()
        p.moveToThreadNext()
        while p and p != after:
            h = p.h
            for tag in ('@menu', '@item'):
                if g.match_word(h, 0, tag):
                    itemName = h[len(tag):].strip()
                    if itemName:
                        if tag == '@menu':
                            aList2 = []
                            kind = '%s' % itemName
                            body = p.b
                            self.doPopupItems(p, aList2)
                            aList.append((kind + '\n' + body, aList2),)
                            p.moveToNodeAfterTree()
                            break
                        else:
                            kind = tag
                            head = itemName
                            body = p.b
                            aList.append((head, body),)
                            p.moveToThreadNext()
                            break
            else:
                p.moveToThreadNext()
    #@+node:ekr.20041121125741: *4* doRatio
    def doRatio(self, p, kind, name, val):
        try:
            val = float(val)
            if 0.0 <= val <= 1.0:
                self.set(p, kind, name, val)
            else:
                self.valueError(p, kind, name, val)
        except ValueError:
            self.valueError(p, kind, name, val)
    #@+node:ekr.20041120105609: *4* doShortcuts (ParserBaseClass)
    def doShortcuts(self, p, kind, junk_name, junk_val, s=None):
        '''Handle an @shortcut or @shortcuts node.'''
        c, d = self.c, self.shortcutsDict
        if s is None: s = p.b
        fn = d.name()
        for line in g.splitLines(s):
            line = line.strip()
            if line and not g.match(line, 0, '#'):
                commandName, bi = self.parseShortcutLine(fn, line)
                if bi is None: # Fix #718.
                    print('\nWarning: bad shortcut specifier: %r\n' % line)
                else:
                    if bi and bi.stroke not in (None, 'none', 'None'):
                        self.doOneShortcut(bi, commandName, p)
                    else:
                        # New in Leo 5.7: Add local assignments to None to c.k.killedBindings.
                        if c.config.isLocalSettingsFile():
                            c.k.killedBindings.append(commandName)
    #@+node:ekr.20111020144401.9585: *5* doOneShortcut (ParserBaseClass)
    def doOneShortcut(self, bi, commandName, p):
        '''Handle a regular shortcut.'''
        d = self.shortcutsDict
        aList = d.get(commandName, [])
        aList.append(bi)
        d[commandName] = aList
    #@+node:ekr.20041217132028: *4* doString
    def doString(self, p, kind, name, val):
        # At present no checking is done.
        self.set(p, kind, name, val)
    #@+node:ekr.20041120094940.8: *4* doStrings
    def doStrings(self, p, kind, name, val):
        '''We expect one of the following:
        @strings aName[val1,val2...]=val
        @strings [val1,val2,...]aName=val'''
        name = name.strip()
        i = name.find('[')
        j = name.find(']')
        if -1 < i < j:
            items = name[i + 1: j]
            items = items.split(',')
            items = [item.strip() for item in items]
            name = name[: i] + name[j + 1:].strip()
            kind = "strings[%s]" % (','.join(items))
            # At present no checking is done.
            self.set(p, kind, name, val)
    #@+node:ekr.20041124063257: *3* munge (ParserBaseClass)
    def munge(self, s):
        return g.app.config.canonicalizeSettingName(s)
    #@+node:ekr.20041119204700.2: *3* oops (ParserBaseClass)
    def oops(self):
        g.pr("ParserBaseClass oops:",
            g.callers(),
            "must be overridden in subclass")
    #@+node:ekr.20041213082558: *3* parsers (ParserBaseClass)
    #@+node:ekr.20041213083651: *4* fontSettingNameToFontKind
    def fontSettingNameToFontKind(self, name):
        s = name.strip()
        if s:
            for tag in ('_family', '_size', '_slant', '_weight'):
                if s.endswith(tag):
                    return tag[1:]
        return None
    #@+node:ekr.20041213082558.1: *4* parseFont & helper
    def parseFont(self, p):
        d = {
            'comments': [],
            'family': None,
            'size': None,
            'slant': None,
            'weight': None,
        }
        s = p.b
        lines = g.splitLines(s)
        for line in lines:
            self.parseFontLine(line, d)
        comments = d.get('comments')
        d['comments'] = '\n'.join(comments)
        return d
    #@+node:ekr.20041213082558.2: *5* parseFontLine
    def parseFontLine(self, line, d):
        s = line.strip()
        if not s: return
        try:
            s = str(s)
        except UnicodeError:
            pass
        if g.match(s, 0, '#'):
            s = s[1:].strip()
            comments = d.get('comments')
            comments.append(s)
            d['comments'] = comments
        else:
            # name is everything up to '='
            i = s.find('=')
            if i == -1:
                name = s; val = None
            else:
                name = s[: i].strip()
                val = s[i + 1:].strip()
                val = val.lstrip('"').rstrip('"')
                val = val.lstrip("'").rstrip("'")
            fontKind = self.fontSettingNameToFontKind(name)
            if fontKind:
                d[fontKind] = name, val # Used only by doFont.
    #@+node:ekr.20041119205148: *4* parseHeadline
    def parseHeadline(self, s):
        """
        Parse a headline of the form @kind:name=val
        Return (kind,name,val).
        Leo 4.11.1: Ignore everything after @data name.
        """
        kind = name = val = None
        if g.match(s, 0, '@'):
            i = g.skip_id(s, 1, chars='-')
            i = g.skip_ws(s, i)
            kind = s[1: i].strip()
            if kind:
                # name is everything up to '='
                if kind == 'data':
                    # i = g.skip_ws(s,i)
                    j = s.find(' ', i)
                    if j == -1:
                        name = s[i:].strip()
                    else:
                        name = s[i: j].strip()
                else:
                    j = s.find('=', i)
                    if j == -1:
                        name = s[i:].strip()
                    else:
                        name = s[i: j].strip()
                        # val is everything after the '='
                        val = s[j + 1:].strip()
        return kind, name, val
    #@+node:ekr.20070411101643.2: *4* parseOpenWith & helper (ParserBaseClass)
    def parseOpenWith(self, p):

        d = {'command': None}
           # d contains args, kind, etc tags.
        for line in g.splitLines(p.b):
            self.parseOpenWithLine(line, d)
        return d
    #@+node:ekr.20070411101643.4: *5* parseOpenWithLine
    def parseOpenWithLine(self, line, d):
        s = line.strip()
        if not s: return
        i = g.skip_ws(s, 0)
        if g.match(s, i, '#'):
            return
        # try:
            # s = str(s)
        # except UnicodeError:
            # pass
        if 1: # new code
            j = g.skip_c_id(s, i)
            tag = s[i: j].strip()
            if not tag:
                g.es_print('@openwith lines must start with a tag: %s' % (s))
                return
            i = g.skip_ws(s, j)
            if not g.match(s, i, ':'):
                g.es_print('colon must follow @openwith tag: %s' % (s))
                return
            i += 1
            val = s[i:].strip() or ''
                # An empty val is valid.
            if tag == 'arg':
                aList = d.get('args', [])
                aList.append(val)
                d['args'] = aList
            elif d.get(tag):
                g.es_print('ignoring duplicate definition of %s %s' % (tag, s))
            else:
                d[tag] = val
        else:
            d['command'] = s
    #@+node:ekr.20041120112043: *4* parseShortcutLine (ParserBaseClass)
    def parseShortcutLine(self, kind, s):
        '''Parse a shortcut line.  Valid forms:

        --> entry-command
        settingName = shortcut
        settingName ! paneName = shortcut
        command-name --> mode-name = binding
        command-name --> same = binding
        '''
        # c = self.c
        s = s.replace('\x7f', '')
            # Can happen on MacOS. Very weird.
        name = val = nextMode = None; nextMode = 'none'
        i = g.skip_ws(s, 0)
        if g.match(s, i, '-->'): # New in 4.4.1 b1: allow mode-entry commands.
            j = g.skip_ws(s, i + 3)
            i = g.skip_id(s, j, '-')
            entryCommandName = s[j: i]
            return None, g.BindingInfo('*entry-command*', commandName=entryCommandName)
        j = i
        i = g.skip_id(s, j, '-@') # #718.
        name = s[j: i]
        # #718: Allow @button- and @command- prefixes.
        for tag in ('@button-', '@command-'):
            if name.startswith(tag):
                name = name[len(tag):]
                break
        if not name:
            return None, None
        # New in Leo 4.4b2.
        i = g.skip_ws(s, i)
        if g.match(s, i, '->'): # New in 4.4: allow pane-specific shortcuts.
            j = g.skip_ws(s, i + 2)
            i = g.skip_id(s, j)
            nextMode = s[j: i]
        i = g.skip_ws(s, i)
        if g.match(s, i, '!'): # New in 4.4: allow pane-specific shortcuts.
            j = g.skip_ws(s, i + 1)
            i = g.skip_id(s, j)
            pane = s[j: i]
            if not pane.strip(): pane = 'all'
        else: pane = 'all'
        i = g.skip_ws(s, i)
        if g.match(s, i, '='):
            i = g.skip_ws(s, i + 1)
            val = s[i:]
        # New in 4.4: Allow comments after the shortcut.
        # Comments must be preceded by whitespace.
        if val:
            i = val.find('#')
            if i > 0 and val[i - 1] in (' ', '\t'):
                val = val[: i].strip()
        if not val:
            return name, None
        stroke = g.KeyStroke(binding=val) if val else None
        bi = g.BindingInfo(
            kind=kind,
            nextMode=nextMode,
            pane=pane,
            stroke=stroke)
        return name, bi
    #@+node:ekr.20041120094940.9: *3* set (ParserBaseClass)
    def set(self, p, kind, name, val):
        """Init the setting for name to val."""
        c = self.c
        # Note: when kind is 'shortcut', name is a command name.
        key = self.munge(name)
        if key is None:
            g.es_print('Empty setting name in', p.h in c.fileName())
            parent = p.parent()
            while parent:
                g.trace('parent', parent.h)
                parent.moveToParent()
            return
        d = self.settingsDict
        gs = d.get(key)
        if gs:
            assert isinstance(gs, g.GeneralSetting), gs
            path = gs.path
            if c.os_path_finalize(c.mFileName) != c.os_path_finalize(path):
                g.es("over-riding setting:", name, "from", path)
        # Important: we can't use c here: it may be destroyed!
        d[key] = g.GeneralSetting(kind, path=c.mFileName, val=val, tag='setting',
            unl=(p and p.get_UNL(with_proto=True)))
    #@+node:ekr.20041119204700.1: *3* traverse (ParserBaseClass)
    def traverse(self, theme=False):
        '''Traverse the entire settings tree.'''
        c = self.c
        self.settingsDict = g.TypedDict(
            name='settingsDict for %s' % (c.shortFileName()),
            keyType=type('settingName'),
            valType=g.GeneralSetting)
        self.shortcutsDict = g.TypedDictOfLists(
            name='shortcutsDict for %s' % (c.shortFileName()),
            keyType=type('s'),
            valType=g.BindingInfo)
        # This must be called after the outline has been inited.
        p = c.config.settingsRoot(theme=theme)
        if not p:
            # c.rootPosition() doesn't exist yet.
            # This is not an error.
            return self.shortcutsDict, self.settingsDict
        after = p.nodeAfterTree()
        while p and p != after:
            result = self.visitNode(p)
            if result == "skip":
                # g.warning('skipping settings in',p.h)
                p.moveToNodeAfterTree()
            else:
                p.moveToThreadNext()
        # Return the raw dict, unmerged.
        return self.shortcutsDict, self.settingsDict
    #@+node:ekr.20041120094940.10: *3* valueError
    def valueError(self, p, kind, name, val):
        """Give an error: val is not valid for kind."""
        self.error("%s is not a valid %s for %s" % (val, kind, name))
    #@+node:ekr.20041119204700.3: *3* visitNode (must be overwritten in subclasses)
    def visitNode(self, p):
        self.oops()
    #@-others
#@-<< class ParserBaseClass >>
#@+others
#@+node:ekr.20041119203941: ** class GlobalConfigManager
class GlobalConfigManager(object):
    """A class to manage configuration settings."""
    #@+<< GlobalConfigManager class data >>
    #@+node:ekr.20041122094813: *3* << GlobalConfigManager class data >>
    #@+others
    #@+node:ekr.20041117062717.1: *4* defaultsDict (GCM class data)
    #@+at This contains only the "interesting" defaults.
    # Ints and bools default to 0, floats to 0.0 and strings to "".
    #@@c
    defaultBodyFontSize = 9 if sys.platform == "win32" else 12
    defaultLogFontSize = 8 if sys.platform == "win32" else 12
    defaultMenuFontSize = 9 if sys.platform == "win32" else 12
    defaultTreeFontSize = 9 if sys.platform == "win32" else 12
    defaultsDict = g.TypedDict(
        name='g.app.config.defaultsDict',
        keyType=type('key'), valType=g.GeneralSetting)
    defaultsData = (
        # compare options...
        ("ignore_blank_lines", "bool", True),
        ("limit_count", "int", 9),
        ("print_mismatching_lines", "bool", True),
        ("print_trailing_lines", "bool", True),
        # find/change options...
        ("search_body", "bool", True),
        ("whole_word", "bool", True),
        # Prefs panel.
        # ("default_target_language","language","python"),
        ("target_language", "language", "python"), # Bug fix: 6/20,2005.
        ("tab_width", "int", -4),
        ("page_width", "int", 132),
        ("output_doc_chunks", "bool", True),
        ("tangle_outputs_header", "bool", True),
        # Syntax coloring options...
        # Defaults for colors are handled by leoColor.py.
        ("color_directives_in_plain_text", "bool", True),
        ("underline_undefined_section_names", "bool", True),
        # Window options...
        ("body_pane_wraps", "bool", True),
        ("body_text_font_family", "family", "Courier"),
        ("body_text_font_size", "size", defaultBodyFontSize),
        ("body_text_font_slant", "slant", "roman"),
        ("body_text_font_weight", "weight", "normal"),
        ("enable_drag_messages", "bool", True),
        ("headline_text_font_family", "string", None),
        ("headline_text_font_size", "size", defaultLogFontSize),
        ("headline_text_font_slant", "slant", "roman"),
        ("headline_text_font_weight", "weight", "normal"),
        ("log_text_font_family", "string", None),
        ("log_text_font_size", "size", defaultLogFontSize),
        ("log_text_font_slant", "slant", "roman"),
        ("log_text_font_weight", "weight", "normal"),
        ("initial_window_height", "int", 600),
        ("initial_window_width", "int", 800),
        ("initial_window_left", "int", 10),
        ("initial_window_top", "int", 10),
        ("initial_split_orientation", "string", "vertical"), # was initial_splitter_orientation.
        ("initial_vertical_ratio", "ratio", 0.5),
        ("initial_horizontal_ratio", "ratio", 0.3),
        ("initial_horizontal_secondary_ratio", "ratio", 0.5),
        ("initial_vertical_secondary_ratio", "ratio", 0.7),
        # ("outline_pane_scrolls_horizontally","bool",False),
        ("split_bar_color", "color", "LightSteelBlue2"),
        ("split_bar_relief", "relief", "groove"),
        ("split_bar_width", "int", 7),
    )
    #@+node:ekr.20041118062709: *4* define encodingIvarsDict (GCM class data)
    encodingIvarsDict = g.TypedDict(
        name='g.app.config.encodingIvarsDict',
        keyType=type('key'), valType=g.GeneralSetting)
    encodingIvarsData = (
        ("default_at_auto_file_encoding", "string", "utf-8"),
        ("default_derived_file_encoding", "string", "utf-8"),
        ("new_leo_file_encoding", "string", "UTF-8"),
            # Upper case for compatibility with previous versions.
        ("defaultEncoding", "string", None),
            # Defaults to None so it doesn't override better defaults.
    )
    #@+node:ekr.20041117072055: *4* ivarsDict (GCM class data)
    # Each of these settings sets the corresponding ivar.
    # Also, the LocalConfigManager class inits the corresponding commander ivar.
    ivarsDict = g.TypedDict(
        name='g.app.config.ivarsDict',
        keyType=type('key'), valType=g.GeneralSetting)
    ivarsData = (
        ("at_root_bodies_start_in_doc_mode", "bool", True),
            # For compatibility with previous versions.
        ("create_nonexistent_directories", "bool", False),
        ("output_initial_comment", "string", ""),
            # "" for compatibility with previous versions.
        ("output_newline", "string", "nl"),
        ("page_width", "int", "132"),
        ("read_only", "bool", True),
        ("redirect_execute_script_output_to_log_pane", "bool", False),
        ("relative_path_base_directory", "string", "!"),
        ("remove_sentinels_extension", "string", ".txt"),
        ("save_clears_undo_buffer", "bool", False),
        ("stylesheet", "string", None),
        ("tab_width", "int", -4),
        ("target_language", "language", "python"),
            # Bug fix: added: 6/20/2005.
        ("trailing_body_newlines", "string", "asis"),
        ("use_plugins", "bool", True),
            # New in 4.3: use_plugins = True by default.
        # ("use_psyco","bool",False),
            # use_pysco can not be set by config code:
            # config processing happens too late.
        ("undo_granularity", "string", "word"),
            # "char","word","line","node"
        ("write_strips_blank_lines", "bool", False),
    )
    #@-others
    #@-<< GlobalConfigManager class data >>
    #@+others
    #@+node:ekr.20041117083202: *3* gcm.Birth...
    #@+node:ekr.20041117062717.2: *4* gcm.ctor
    def __init__(self):
        #
        # Set later.  To keep pylint happy.
        if 0: # No longer needed, now that setIvarsFromSettings always sets gcm ivars.
            self.at_root_bodies_start_in_doc_mode = True
            self.default_derived_file_encoding = 'utf-8'
            self.output_newline = 'nl'
            self.redirect_execute_script_output_to_log_pane = True
            self.relative_path_base_directory = '!'
        self.use_plugins = False # Required to keep pylint happy.
        self.create_nonexistent_directories = False # Required to keep pylint happy.
        self.atCommonButtonsList = [] # List of info for common @buttons nodes.
        self.atCommonCommandsList = [] # List of info for common @commands nodes.
        self.atLocalButtonsList = [] # List of positions of @button nodes.
        self.atLocalCommandsList = [] # List of positions of @command nodes.
        self.buttonsFileName = ''
        self.configsExist = False # True when we successfully open a setting file.
        self.unitTestDict = {} # For unit testing: *not* the same as g.app.unitTestDict.
        self.defaultFont = None # Set in gui.getDefaultConfigFont.
        self.defaultFontFamily = None # Set in gui.getDefaultConfigFont.
        self.enabledPluginsFileName = None
        self.enabledPluginsString = ''
        self.inited = False
        self.menusList = []
        self.menusFileName = ''
        self.modeCommandsDict = g.TypedDict(
            name='modeCommandsDict',
            keyType=type('commandName'),
            valType=g.TypedDictOfLists)
        # Inited later...
        self.panes = None
        self.sc = None
        self.tree = None
        self.initDicts()
        self.initIvarsFromSettings()
        self.initRecentFiles()
    #@+node:ekr.20041227063801.2: *4* gcm.initDicts
    def initDicts(self):
        # Only the settings parser needs to search all dicts.
        self.dictList = [self.defaultsDict]
        for key, kind, val in self.defaultsData:
            self.defaultsDict[self.munge(key)] = g.GeneralSetting(
                kind, setting=key, val=val, tag='defaults')
        for key, kind, val in self.ivarsData:
            self.ivarsDict[self.munge(key)] = g.GeneralSetting(
                kind, ivar=key, val=val, tag='ivars')
        for key, kind, val in self.encodingIvarsData:
            self.encodingIvarsDict[self.munge(key)] = g.GeneralSetting(
                kind, encoding=val, ivar=key, tag='encoding')
    #@+node:ekr.20041117065611.2: *4* gcm.initIvarsFromSettings & helpers
    def initIvarsFromSettings(self):
        for ivar in sorted(list(self.encodingIvarsDict.keys())):
            self.initEncoding(ivar)
        for ivar in sorted(list(self.ivarsDict.keys())):
            self.initIvar(ivar)
    #@+node:ekr.20041117065611.1: *5* initEncoding
    def initEncoding(self, key):
        '''Init g.app.config encoding ivars during initialization.'''
        # Important: The key is munged.
        gs = self.encodingIvarsDict.get(key)
        setattr(self, gs.ivar, gs.encoding)
        if gs.encoding and not g.isValidEncoding(gs.encoding):
            g.es("g.app.config: bad encoding:", "%s: %s" % (gs.ivar, gs.encoding))
    #@+node:ekr.20041117065611: *5* initIvar
    def initIvar(self, key):
        '''Init g.app.config ivars during initialization.

        This does NOT init the corresponding commander ivars.

        Such initing must be done in setIvarsFromSettings.'''
        # Important: the key is munged.
        d = self.ivarsDict
        gs = d.get(key)
        setattr(self, gs.ivar, gs.val)
    #@+node:ekr.20041117083202.2: *4* gcm.initRecentFiles
    def initRecentFiles(self):
        self.recentFiles = []
    #@+node:ekr.20041228042224: *4* gcm.setIvarsFromSettings
    def setIvarsFromSettings(self, c):
        '''Init g.app.config ivars or c's ivars from settings.

        - Called from c.initSettings with c = None to init g.app.config ivars.
        - Called from c.initSettings to init corresponding commmander ivars.
        '''
        if g.app.loadedThemes:
            return
        if not self.inited:
            return
        # Ignore temporary commanders created by readSettingsFiles.
        d = self.ivarsDict
        keys = list(d.keys())
        keys.sort()
        for key in keys:
            gs = d.get(key)
            if gs:
                assert isinstance(gs, g.GeneralSetting)
                ivar = gs.ivar # The actual name of the ivar.
                kind = gs.kind
                if c:
                    val = c.config.get(key, kind)
                else:
                    val = self.get(key, kind) # Don't use bunch.val!
                if c:
                    setattr(c, ivar, val)
                if True: # Always set the global ivars.
                    setattr(self, ivar, val)
    #@+node:ekr.20041117081009: *3* gcm.Getters...
    #@+node:ekr.20041123070429: *4* gcm.canonicalizeSettingName (munge)
    def canonicalizeSettingName(self, name):
        if name is None:
            return None
        name = name.lower()
        for ch in ('-', '_', ' ', '\n'):
            name = name.replace(ch, '')
        return name if name else None

    munge = canonicalizeSettingName
    #@+node:ekr.20051011105014: *4* gcm.exists
    def exists(self, setting, kind):
        '''Return true if a setting of the given kind exists, even if it is None.'''
        lm = g.app.loadManager
        d = lm.globalSettingsDict
        if d:
            junk, found = self.getValFromDict(d, setting, kind)
            return found
        else:
            return False
    #@+node:ekr.20041117083141: *4* gcm.get & allies
    def get(self, setting, kind):
        """Get the setting and make sure its type matches the expected type."""
        lm = g.app.loadManager
        #
        # It *is* valid to call this method: it returns the global settings.
        d = lm.globalSettingsDict
        if d:
            assert g.isTypedDict(d), d
            val, junk = self.getValFromDict(d, setting, kind)
            return val
        else:
            return None
    #@+node:ekr.20041121143823: *5* gcm.getValFromDict
    def getValFromDict(self, d, setting, requestedType, warn=True):
        '''Look up the setting in d. If warn is True, warn if the requested type
        does not (loosely) match the actual type.
        returns (val,exists)'''
        gs = d.get(self.munge(setting))
        if not gs: return None, False
        assert isinstance(gs, g.GeneralSetting)
        val = gs.val
        # 2011/10/24: test for an explicit None.
        if g.isPython3:
            isNone = val in ('None', 'none', '') # ,None)
        else:
            isNone = val in (
                g.u('None'), g.u('none'), g.u(''),
                'None', 'none', '')
        if not self.typesMatch(gs.kind, requestedType):
            # New in 4.4: make sure the types match.
            # A serious warning: one setting may have destroyed another!
            # Important: this is not a complete test of conflicting settings:
            # The warning is given only if the code tries to access the setting.
            if warn:
                g.error('warning: ignoring', gs.kind, '', setting, 'is not', requestedType)
                g.error('there may be conflicting settings!')
            return None, False
        # elif val in (u'None',u'none','None','none','',None):
        elif isNone:
            return '', True
                # 2011/10/24: Exists, a *user-defined* empty value.
        else:
            return val, True
    #@+node:ekr.20051015093141: *5* gcm.typesMatch
    def typesMatch(self, type1, type2):
        '''
        Return True if type1, the actual type, matches type2, the requeseted type.

        The following equivalences are allowed:

        - None matches anything.
        - An actual type of string or strings matches anything *except* shortcuts.
        - Shortcut matches shortcuts.
        '''
        # The shortcuts logic no longer uses the get/set code.
        shortcuts = ('shortcut', 'shortcuts',)
        if type1 in shortcuts or type2 in shortcuts:
            g.trace('oops: type in shortcuts')
        return (
            type1 is None or type2 is None or
            type1.startswith('string') and type2 not in shortcuts or
            type1 == 'int' and type2 == 'size' or
            (type1 in shortcuts and type2 in shortcuts) or
            type1 == type2
        )
    #@+node:ekr.20060608224112: *4* gcm.getAbbrevDict
    def getAbbrevDict(self):
        """Search all dictionaries for the setting & check it's type"""
        d = self.get('abbrev', 'abbrev')
        return d or {}
    #@+node:ekr.20041117081009.3: *4* gcm.getBool
    def getBool(self, setting, default=None):
        '''Return the value of @bool setting, or the default if the setting is not found.'''
        val = self.get(setting, "bool")
        if val in (True, False):
            return val
        else:
            return default
    #@+node:ekr.20070926082018: *4* gcm.getButtons
    def getButtons(self):
        '''Return a list of tuples (x,y) for common @button nodes.'''
        return g.app.config.atCommonButtonsList
    #@+node:ekr.20041122070339: *4* gcm.getColor
    def getColor(self, setting):
        '''Return the value of @color setting.'''
        col = self.get(setting, "color")
        while col and col.startswith('@'):
            col = self.get(col[1:], "color")
        return col
    #@+node:ekr.20080312071248.7: *4* gcm.getCommonCommands
    def getCommonAtCommands(self):
        '''Return the list of tuples (headline,script) for common @command nodes.'''
        return g.app.config.atCommonCommandsList
    #@+node:ekr.20071214140900.1: *4* gcm.getData & getOutlineData
    def getData(self, setting, strip_comments=True, strip_data=True):
        '''Return a list of non-comment strings in the body text of @data setting.'''
        data = self.get(setting, "data")
        # New in Leo 4.12.1: add two keyword arguments, with legacy defaults.
        if data and strip_comments:
            data = [z for z in data if not z.strip().startswith('#')]
        if data and strip_data:
            data = [z.strip() for z in data if z.strip()]
        return data

    def getOutlineData(self, setting):
        '''Return the pastable (xml text) of the entire @outline-data tree.'''
        return self.get(setting, "outlinedata")
    #@+node:ekr.20041117093009.1: *4* gcm.getDirectory
    def getDirectory(self, setting):
        '''Return the value of @directory setting, or None if the directory does not exist.'''
        # Fix https://bugs.launchpad.net/leo-editor/+bug/1173763
        theDir = self.get(setting, 'directory')
        if g.os_path_exists(theDir) and g.os_path_isdir(theDir):
            return theDir
        else:
            return None
    #@+node:ekr.20070224075914.1: *4* gcm.getEnabledPlugins
    def getEnabledPlugins(self):
        '''Return the body text of the @enabled-plugins node.'''
        return g.app.config.enabledPluginsString
    #@+node:ekr.20041117082135: *4* gcm.getFloat
    def getFloat(self, setting):
        '''Return the value of @float setting.'''
        val = self.get(setting, "float")
        try:
            val = float(val)
            return val
        except TypeError:
            return None
    #@+node:ekr.20041117062717.13: *4* gcm.getFontFromParams
    def getFontFromParams(self, family, size, slant, weight, defaultSize=12):
        """Compute a font from font parameters.

        Arguments are the names of settings to be use.
        Default to size=12, slant="roman", weight="normal".

        Return None if there is no family setting so we can use system default fonts."""
        family = self.get(family, "family")
        if family in (None, ""):
            family = self.defaultFontFamily
        size = self.get(size, "size")
        if size in (None, 0): size = defaultSize
        slant = self.get(slant, "slant")
        if slant in (None, ""): slant = "roman"
        weight = self.get(weight, "weight")
        if weight in (None, ""): weight = "normal"
        return g.app.gui.getFontFromParams(family, size, slant, weight)
    #@+node:ekr.20041117081513: *4* gcm.getInt
    def getInt(self, setting):
        '''Return the value of @int setting.'''
        val = self.get(setting, "int")
        try:
            val = int(val)
            return val
        except TypeError:
            return None
    #@+node:ekr.20041117093009.2: *4* gcm.getLanguage
    def getLanguage(self, setting):
        '''Return the setting whose value should be a language known to Leo.'''
        language = self.getString(setting)
        return language
    #@+node:ekr.20070926070412: *4* gcm.getMenusList
    def getMenusList(self):
        '''Return the list of entries for the @menus tree.'''
        aList = self.get('menus', 'menus')
        # aList is typically empty.
        return aList or g.app.config.menusList
    #@+node:ekr.20070411101643: *4* gcm.getOpenWith
    def getOpenWith(self):
        '''Return a list of dictionaries corresponding to @openwith nodes.'''
        val = self.get('openwithtable', 'openwithtable')
        return val
    #@+node:ekr.20041122070752: *4* gcm.getRatio
    def getRatio(self, setting):
        '''Return the value of @float setting.

        Warn if the value is less than 0.0 or greater than 1.0.'''
        val = self.get(setting, "ratio")
        try:
            val = float(val)
            if 0.0 <= val <= 1.0:
                return val
            else:
                return None
        except TypeError:
            return None
    #@+node:ekr.20041117062717.11: *4* gcm.getRecentFiles
    def getRecentFiles(self):
        '''Return the list of recently opened files.'''
        return self.recentFiles
    #@+node:ekr.20041117081009.4: *4* gcm.getString
    def getString(self, setting):
        '''Return the value of @string setting.'''
        return self.get(setting, "string")
    #@+node:ekr.20120222103014.10314: *3* gcm.config_iter
    def config_iter(self, c):
        '''Letters:
          leoSettings.leo
        D default settings
        F loaded .leo File
        M myLeoSettings.leo
        @ @button, @command, @mode.
        '''
        lm = g.app.loadManager
        d = c.config.settingsDict if c else lm.globalSettingsDict
        limit = c.config.getInt('print-settings-at-data-limit')
        if limit is None:
            limit = 20 # A resonable default.
        # pylint: disable=len-as-condition
        for key in sorted(list(d.keys())):
            gs = d.get(key)
            assert g.isGeneralSetting(gs), gs
            if gs and gs.kind:
                letter = lm.computeBindingLetter(gs.path)
                val = gs.val
                if gs.kind == 'data':
                    # #748: Remove comments
                    aList = [' '*8 + z.rstrip() for z in val
                        if z.strip() and not z.strip().startswith('#')]
                    if not aList:
                        val = '[]'
                    elif limit == 0 or len(aList) < limit:
                        val = '\n    [\n' + '\n'.join(aList) + '\n    ]'
                        # The following doesn't work well.
                        # val = g.objToString(aList, indent=' '*4)
                    else:
                        val = '<%s non-comment lines>' % len(aList)
                elif g.isString(val) and val.startswith('<?xml'):
                    val = '<xml>'
                key2 = '@%-6s %s' % (gs.kind, key)
                yield key2, val, c, letter
    #@+node:ekr.20171115062202.1: *3* gcm.valueInMyLeoSettings
    def valueInMyLeoSettings(self, settingName):
        '''Return the value of the setting, if any, in myLeoSettings.leo.'''
        lm = g.app.loadManager
        d = lm.globalSettingsDict.d
        gs = d.get(self.munge(settingName))
            # A GeneralSetting object.
        if gs:
            path = gs.path
            if path.find('myLeoSettings.leo') > -1:
                return gs.val
        return None
    #@-others
#@+node:ekr.20041118104831.1: ** class LocalConfigManager
class LocalConfigManager(object):
    """A class to hold config settings for commanders."""
    #@+others
    #@+node:ekr.20120215072959.12472: *3* c.config.Birth
    #@+node:ekr.20041118104831.2: *4* c.config.ctor
    def __init__(self, c, previousSettings=None):

        self.c = c
        lm = g.app.loadManager
        #
        # c.__init__ and helpers set the shortcuts and settings dicts for local files.
        if previousSettings:
            self.settingsDict = previousSettings.settingsDict
            self.shortcutsDict = previousSettings.shortcutsDict
            assert g.isTypedDict(self.settingsDict)
            assert g.isTypedDictOfLists(self.shortcutsDict)
        else:
            self.settingsDict = d1 = lm.globalSettingsDict
            self.shortcutsDict = d2 = lm.globalBindingsDict
            assert d1 is None or g.isTypedDict(d1), d1
            assert d2 is None or g.isTypedDictOfLists(d2), d2
        # Define these explicitly to eliminate a pylint warning.
        if 0:
            # No longer needed now that c.config.initIvar always sets
            # both c and c.config ivars.
            self.default_derived_file_encoding = g.app.config.default_derived_file_encoding
            self.redirect_execute_script_output_to_log_pane = g.app.config.redirect_execute_script_output_to_log_pane
        self.defaultBodyFontSize = g.app.config.defaultBodyFontSize
        self.defaultLogFontSize = g.app.config.defaultLogFontSize
        self.defaultMenuFontSize = g.app.config.defaultMenuFontSize
        self.defaultTreeFontSize = g.app.config.defaultTreeFontSize
        for key in sorted(list(g.app.config.encodingIvarsDict.keys())):
            self.initEncoding(key)
        for key in sorted(list(g.app.config.ivarsDict.keys())):
            self.initIvar(key)
    #@+node:ekr.20041118104414: *4* c.config.initEncoding
    def initEncoding(self, key):
        # Important: the key is munged.
        gs = g.app.config.encodingIvarsDict.get(key)
        encodingName = gs.ivar
        encoding = self.get(encodingName, kind='string')
        # Use the global setting as a last resort.
        if encoding:
            setattr(self, encodingName, encoding)
        else:
            encoding = getattr(g.app.config, encodingName)
            setattr(self, encodingName, encoding)
        if encoding and not g.isValidEncoding(encoding):
            g.es("bad", "%s: %s" % (encodingName, encoding))
    #@+node:ekr.20041118104240: *4* c.config.initIvar
    def initIvar(self, key):

        c = self.c
        # Important: the key is munged.
        gs = g.app.config.ivarsDict.get(key)
        ivarName = gs.ivar
        val = self.get(ivarName, kind=None)
        if val or not hasattr(self, ivarName):
            # Set *both* the commander ivar and the c.config ivar.
            setattr(self, ivarName, val)
            setattr(c, ivarName, val)
    #@+node:ekr.20120215072959.12471: *3* c.config.Getters
    #@+node:ekr.20041123092357: *4* c.config.findSettingsPosition & helper
    # This was not used prior to Leo 4.5.

    def findSettingsPosition(self, setting):
        """Return the position for the setting in the @settings tree for c."""
        munge = g.app.config.munge
        # c = self.c
        root = self.settingsRoot()
        if not root:
            return None
        setting = munge(setting)
        for p in root.subtree():
            #BJ munge will return None if a headstring is empty
            h = munge(p.h) or ''
            if h.startswith(setting):
                return p.copy()
        return None
    #@+node:ekr.20041120074536: *5* c.config.settingsRoot
    def settingsRoot(self, theme=False):
        '''Return the position of the @settings tree.'''
        c = self.c
        for p in c.all_unique_positions():
            if p.h.rstrip() == "@settings":
                if not theme:
                    return p.copy()
                # Look for an inner @theme node
                for p2 in p.subtree():
                    if g.match_word(p2.h, 0, '@theme'):
                        return p2.copy()
        return None
    #@+node:ekr.20120215072959.12515: *4* c.config.Getters
    #@@nocolor-node
    #@+at Only the following need to be defined.
    # 
    #     get (self,setting,theType)
    #     getAbbrevDict (self)
    #     getBool (self,setting,default=None)
    #     getButtons (self)
    #     getColor (self,setting)
    #     getData (self,setting)
    #     getDirectory (self,setting)
    #     getFloat (self,setting)
    #     getFontFromParams (self,family,size,slant,weight,defaultSize=12)
    #     getInt (self,setting)
    #     getLanguage (self,setting)
    #     getMenusList (self)
    #     getOutlineData (self)
    #     getOpenWith (self)
    #     getRatio (self,setting)
    #     getShortcut (self,commandName)
    #     getString (self,setting)
    #@+node:ekr.20120215072959.12519: *5* c.config.get & allies
    def get(self, setting, kind):
        """Get the setting and make sure its type matches the expected type."""
        d = self.settingsDict
        if d:
            assert g.isTypedDict(d), d
            val, junk = self.getValFromDict(d, setting, kind)
            return val
        else:
            return None
    #@+node:ekr.20120215072959.12520: *6* getValFromDict
    def getValFromDict(self, d, setting, requestedType, warn=True):
        '''Look up the setting in d. If warn is True, warn if the requested type
        does not (loosely) match the actual type.
        returns (val,exists)'''
        gs = d.get(g.app.config.munge(setting))
        if not gs: return None, False
        assert g.isGeneralSetting(gs), gs
        val = gs.val
        # 2011/10/24: test for an explicit None.
        if g.isPython3:
            isNone = val in ('None', 'none', '') # ,None)
        else:
            isNone = val in (
                g.u('None'), g.u('none'), g.u(''),
                'None', 'none', '') #,None)
        if not self.typesMatch(gs.kind, requestedType):
            # New in 4.4: make sure the types match.
            # A serious warning: one setting may have destroyed another!
            # Important: this is not a complete test of conflicting settings:
            # The warning is given only if the code tries to access the setting.
            if warn:
                g.error('warning: ignoring', gs.kind, '', setting, 'is not', requestedType)
                g.error('there may be conflicting settings!')
            return None, False
        elif isNone:
            return '', True
                # 2011/10/24: Exists, a *user-defined* empty value.
        else:
            return val, True
    #@+node:ekr.20120215072959.12521: *6* typesMatch
    def typesMatch(self, type1, type2):
        '''
        Return True if type1, the actual type, matches type2, the requeseted type.

        The following equivalences are allowed:

        - None matches anything.
        - An actual type of string or strings matches anything *except* shortcuts.
        - Shortcut matches shortcuts.
        '''
        # The shortcuts logic no longer uses the get/set code.
        shortcuts = ('shortcut', 'shortcuts',)
        if type1 in shortcuts or type2 in shortcuts:
            g.trace('oops: type in shortcuts')
        return (
            type1 is None or type2 is None or
            type1.startswith('string') and type2 not in shortcuts or
            type1 == 'int' and type2 == 'size' or
            (type1 in shortcuts and type2 in shortcuts) or
            type1 == type2
        )
    #@+node:ekr.20120215072959.12522: *5* c.config.getAbbrevDict
    def getAbbrevDict(self):
        """Search all dictionaries for the setting & check it's type"""
        d = self.get('abbrev', 'abbrev')
        return d or {}
    #@+node:ekr.20120215072959.12523: *5* c.config.getBool
    def getBool(self, setting, default=None):
        '''Return the value of @bool setting, or the default if the setting is not found.'''
        val = self.get(setting, "bool")
        if val in (True, False):
            return val
        else:
            return default
    #@+node:ekr.20120215072959.12525: *5* c.config.getColor
    def getColor(self, setting):
        '''Return the value of @color setting.'''
        col = self.get(setting, "color")
        while col and col.startswith('@'):
            col = self.get(col[1:], "color")
        return col
    #@+node:ekr.20120215072959.12527: *5* c.config.getData
    def getData(self, setting, strip_comments=True, strip_data=True):
        '''Return a list of non-comment strings in the body text of @data setting.'''
        # 904: Add local abbreviations to global settings.
        append = setting == 'global-abbreviations'
        if append:
            data0 = g.app.config.getData(setting,
                strip_comments=strip_comments,
                strip_data=strip_data,
            )
        data = self.get(setting, "data")
        # New in Leo 4.11: parser.doData strips only comments now.
        # New in Leo 4.12: parser.doData strips *nothing*.
        if g.isString(data):
            data = [data]
        if data and strip_comments:
            data = [z for z in data if not z.strip().startswith('#')]
        if data and strip_data:
            data = [z.strip() for z in data if z.strip()]
        if append and data != data0:
            if data:
                data.extend(data0)
            else:
                data = data0
        return data
    #@+node:ekr.20131114051702.16542: *5* c.config.getOutlineData
    def getOutlineData(self, setting):
        '''Return the pastable (xml) text of the entire @outline-data tree.'''
        data = self.get(setting, "outlinedata")
        if setting == 'tree-abbreviations':
            # 904: Append local tree abbreviations to the global abbreviations.
            data0 = g.app.config.getOutlineData(setting)
            if data and data0 and data != data0:
                assert g.isString(data0)
                assert g.isString(data)
                # We can't merge the data here: they are .leo files!
                # abbrev.init_tree_abbrev_helper does the merge.
                data = [data0, data]
        return data
    #@+node:ekr.20120215072959.12528: *5* c.config.getDirectory
    def getDirectory(self, setting):
        '''Return the value of @directory setting, or None if the directory does not exist.'''
        # Fix https://bugs.launchpad.net/leo-editor/+bug/1173763
        theDir = self.get(setting, 'directory')
        if g.os_path_exists(theDir) and g.os_path_isdir(theDir):
            return theDir
        else:
            return None
    #@+node:ekr.20120215072959.12530: *5* c.config.getFloat
    def getFloat(self, setting):
        '''Return the value of @float setting.'''
        val = self.get(setting, "float")
        try:
            val = float(val)
            return val
        except TypeError:
            return None
    #@+node:ekr.20120215072959.12531: *5* c.config.getFontFromParams
    def getFontFromParams(self, family, size, slant, weight, defaultSize=12):
        """
        Compute a font from font parameters. This should be used *only*
        by the syntax coloring code.  Otherwise, use Leo's style sheets.

        Arguments are the names of settings to be use.
        Default to size=12, slant="roman", weight="normal".

        Return None if there is no family setting so we can use system default fonts.
        """
        family = self.get(family, "family")
        if family in (None, ""):
            family = g.app.config.defaultFontFamily
        size = self.get(size, "size")
        if size in (None, 0):
            size = defaultSize
        slant = self.get(slant, "slant")
        if slant in (None, ""):
            slant = "roman"
        weight = self.get(weight, "weight")
        if weight in (None, ""):
            weight = "normal"
        return g.app.gui.getFontFromParams(family, size, slant, weight)
    #@+node:ekr.20120215072959.12532: *5* c.config.getInt
    def getInt(self, setting):
        '''Return the value of @int setting.'''
        val = self.get(setting, "int")
        try:
            val = int(val)
            return val
        except TypeError:
            return None
    #@+node:ekr.20120215072959.12533: *5* c.config.getLanguage
    def getLanguage(self, setting):
        '''Return the setting whose value should be a language known to Leo.'''
        language = self.getString(setting)
        return language
    #@+node:ekr.20120215072959.12534: *5* c.config.getMenusList
    def getMenusList(self):
        '''Return the list of entries for the @menus tree.'''
        aList = self.get('menus', 'menus')
        # aList is typically empty.
        return aList or g.app.config.menusList
    #@+node:ekr.20120215072959.12535: *5* c.config.getOpenWith
    def getOpenWith(self):
        '''Return a list of dictionaries corresponding to @openwith nodes.'''
        val = self.get('openwithtable', 'openwithtable')
        return val
    #@+node:ekr.20120215072959.12536: *5* c.config.getRatio
    def getRatio(self, setting):
        '''Return the value of @float setting.

        Warn if the value is less than 0.0 or greater than 1.0.'''
        val = self.get(setting, "ratio")
        try:
            val = float(val)
            if 0.0 <= val <= 1.0:
                return val
            else:
                return None
        except TypeError:
            return None
    #@+node:ekr.20120215072959.12538: *5* c.config.getSettingSource
    def getSettingSource(self, setting):
        '''return the name of the file responsible for setting.'''
        d = self.settingsDict
        if d:
            assert g.isTypedDict(d), d
            bi = d.get(setting)
            if bi is None:
                return 'unknown setting', None
            else:
                return bi.path, bi.val
        else:
            # lm.readGlobalSettingsFiles is opening a settings file.
            # lm.readGlobalSettingsFiles has not yet set lm.globalSettingsDict.
            assert d is None
            return None
    #@+node:ekr.20120215072959.12539: *5* c.config.getShortcut
    def getShortcut(self, commandName):
        '''Return rawKey,accel for shortcutName'''
        c = self.c
        d = self.shortcutsDict
        if not c.frame.menu:
            g.trace('no menu: %s' % (commandName))
            return None, []
        if d:
            assert g.isTypedDictOfLists(d), d
            key = c.frame.menu.canonicalizeMenuName(commandName)
            key = key.replace('&', '') # Allow '&' in names.
            aList = d.get(commandName, [])
            if aList: # A list of g.BindingIndo objects.
                # It's important to filter empty strokes here.
                aList = [z for z in aList
                    if z.stroke and z.stroke.lower() != 'none']
            return key, aList
        else:
            # lm.readGlobalSettingsFiles is opening a settings file.
            # lm.readGlobalSettingsFiles has not yet set lm.globalSettingsDict.
            return None, []
    #@+node:ekr.20120215072959.12540: *5* c.config.getString
    def getString(self, setting):
        '''Return the value of @string setting.'''
        return self.get(setting, "string")
    #@+node:ekr.20120215072959.12543: *4* c.config.Getters: redirect to g.app.config
    def getButtons(self):
        '''Return a list of tuples (x,y) for common @button nodes.'''
        return g.app.config.atCommonButtonsList # unusual.

    def getCommands(self):
        '''Return the list of tuples (headline,script) for common @command nodes.'''
        return g.app.config.atCommonCommandsList # unusual.

    def getEnabledPlugins(self):
        '''Return the body text of the @enabled-plugins node.'''
        return g.app.config.enabledPluginsString # unusual.

    def getRecentFiles(self):
        '''Return the list of recently opened files.'''
        return g.app.config.getRecentFiles() # unusual
    #@+node:ekr.20140114145953.16691: *4* c.config.isLocalSetting
    def isLocalSetting(self, setting, kind):
        '''Return True if the indicated setting comes from a local .leo file.'''
        if not kind or kind in ('shortcut', 'shortcuts', 'openwithtable'):
            return False
        key = g.app.config.munge(setting)
        if key is None:
            return False
        gs = self.settingsDict.get(key)
        if not gs:
            return False
        assert g.isGeneralSetting(gs), gs
        path = gs.path.lower()
        for fn in ('myLeoSettings.leo', 'leoSettings.leo'):
            if path.endswith(fn.lower()):
                return False
        return True
    #@+node:ekr.20171119222458.1: *4* c.config.isLocalSettingsFile (new)
    def isLocalSettingsFile(self):
        '''Return true if c is not leoSettings.leo or myLeoSettings.leo'''
        c = self.c
        fn = c.shortFileName().lower()
        for fn2 in ('leoSettings.leo', 'myLeoSettings.leo'):
            if fn.endswith(fn2.lower()):
                return False
        return True
    #@+node:ekr.20120224140548.10528: *4* c.exists (new)
    def exists(self, c, setting, kind):
        '''Return true if a setting of the given kind exists, even if it is None.'''
        d = self.settingsDict
        if d:
            junk, found = self.getValFromDict(d, setting, kind)
            if found: return True
        return False
    #@+node:ekr.20070418073400: *3* c.config.printSettings
    def printSettings(self):
        '''Prints the value of every setting, except key bindings and commands and open-with tables.
        The following shows where the active setting came from:

        -     leoSettings.leo,
        -  @  @button, @command, @mode.
        - [D] default settings.
        - [F] indicates the file being loaded,
        - [M] myLeoSettings.leo,

        '''
        legend = '''\
    legend:
        leoSettings.leo
     @  @button, @command, @mode
    [D] default settings
    [F] loaded .leo File
    [M] myLeoSettings.leo
    '''
        c = self.c
        legend = g.adjustTripleString(legend, c.tab_width)
        result = []
        for name, val, c, letter in g.app.config.config_iter(c):
            kind = '   ' if letter == ' ' else '[%s]' % (letter)
            result.append('%s %s = %s\n' % (kind, name, val))
        # Use a single g.es statement.
        result.append('\n' + legend)
        if g.unitTesting:
            pass # print(''.join(result))
        else:
            g.es_print('', ''.join(result), tabName='Settings')
    #@+node:ekr.20120215072959.12475: *3* c.config.set
    def set(self, p, kind, name, val, warn=True):
        """Init the setting for name to val."""
        c = self.c
        # Note: when kind is 'shortcut', name is a command name.
        key = g.app.config.munge(name)
        d = self.settingsDict
        assert g.isTypedDict(d), d
        gs = d.get(key)
        if gs:
            assert g.isGeneralSetting(gs), gs
            path = gs.path
            if warn and c.os_path_finalize(c.mFileName) != c.os_path_finalize(path):
                g.es("over-riding setting:", name, "from", path)
        gs = g.GeneralSetting(kind, path=c.mFileName, val=val, tag='setting')
        d.replace(key, gs)
    #@+node:ekr.20180121135120.1: *3* c.config.setUserSetting
    def setUserSetting(self, setting, value):
        '''
        Find and set the indicated setting, either in the local file or in
        myLeoSettings.leo.
        '''
        c = self.c
        p = self.findSettingsPosition(setting)
        if not p:
            c = c.openMyLeoSettings()
            if not c: return
            p = c.config.findSettingsPosition(setting)
        if not p:
            root = c.config.settingsRoot()
            if not root: return
            p = c.config.findSettingsPosition(setting)
            if not p:
                p = root.insertAsLastChild()
        h = setting
        i = h.find('=')
        if i > -1:
            h = h[:i].strip()
        p.h = '%s = %s' % (h, value)
        #
        # Delay the second redraw until idle time.
        c.setChanged(redrawFlag=False)
        p.setDirty()
        c.redraw_later()
       
    #@-others
#@+node:ekr.20041119203941.3: ** class SettingsTreeParser (ParserBaseClass)
class SettingsTreeParser(ParserBaseClass):
    '''A class that inits settings found in an @settings tree.

    Used by read settings logic.'''
    #@+others
    #@+node:ekr.20041119204103: *3* ctor (SettingsTreeParser)
    def __init__(self, c, localFlag=True):
        # Init the base class.
        ParserBaseClass.__init__(self, c, localFlag)
    #@+node:ekr.20041119204714: *3* visitNode (SettingsTreeParser)
    def visitNode(self, p):
        """Init any settings found in node p."""
        p = p.copy()
            # Bug fix 2011/11/24
            # Ensure inner traversals don't change callers's p.
        munge = g.app.config.munge
        kind, name, val = self.parseHeadline(p.h)
        kind = munge(kind)
        if g.isPython3:
            isNone = val in ('None', 'none', '', None)
        else:
            isNone = val in (
                g.u('None'), g.u('none'), g.u(''),
                'None', 'none', '', None)
        if kind is None: # Not an @x node. (New in Leo 4.4.4)
            pass
        elif kind == "settings":
            pass
        # elif kind in self.basic_types and val in (u'None',u'none','None','none','',None):
        elif kind in self.basic_types and isNone:
            # None is valid for all basic types.
            self.set(p, kind, name, None)
        elif kind in self.control_types or kind in self.basic_types:
            f = self.dispatchDict.get(kind)
            if f:
                try:
                    return f(p, kind, name, val)
                except Exception:
                    g.es_exception()
            else:
                g.pr("*** no handler", kind)
        return None
    #@-others
#@+node:ekr.20171229131953.1: ** parseFont (leoConfig.py)
def parseFont(b):
    family = None
    weight = None
    slant = None
    size = None
    settings_name = None
    for line in g.splitLines(b):
        line = line.strip()
        if line.startswith('#'): continue
        i = line.find('=')
        if i < 0: continue
        name = line[:i].strip()
        if name.endswith('_family'):
            family = line[i+1:].strip()
        elif name.endswith('_weight'):
            weight = line[i+1:].strip()
        elif name.endswith('_size'):
            size = line[i+1:].strip()
            try:
                size = float(size)
            except ValueError:
                size = 12
        elif name.endswith('_slant'):
            slant = line[i+1:].strip()
        if settings_name is None and name.endswith(('_family', '_slant', '_weight','_size')):
            settings_name = name.rsplit('_', 1)[0]
    return settings_name, family, weight == 'bold', slant in ('slant', 'italic'), size
#@-others
#@@language python
#@@tabwidth -4
#@@pagewidth 70
#@-leo
