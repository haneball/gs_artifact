<template>
  <div id="content-box">
    <el-row :gutter="20">
      <el-col :span="6">
        <el-select v-model="element" placeholder="元素" size="medium" @change="createTargetChar()">
          <el-option v-for="item in elementList" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
      </el-col>
      <el-col :span="6">
        <el-select v-model="charName" placeholder="角色" size="medium" @change="setChar();setMode();createTargetWeapon()">
          <el-option v-for="item in targetChar" :key="item.id" :label="item.name" :value="item.name"></el-option>
        </el-select>
      </el-col>
      <el-col :span="6">
        <el-select v-model="level" placeholder="等级" size="medium" @change="setProperty();countStats()">
          <el-option v-for="item in levelList" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
      </el-col>
      <el-col :span="6">
        <el-select v-model="weaponName" placeholder="武器" size="medium" @change="setWeapon();countStats()">
          <el-option v-for="item in targerWeapon" :key="item.id" :label="item.name" :value="item.name"></el-option>
        </el-select>
      </el-col>
    </el-row>
    <el-row :gutter="60">
      <el-col :span="8">
        <el-select v-model="nowArtifact[0]" placeholder="时之沙" size="medium" @change="setArtifact();countStats()">
          <el-option label="生命值" value="hp"></el-option>
          <el-option label="攻击力" value="atk"></el-option>
          <el-option label="防御力" value="def"></el-option>
          <el-option label="元素精通" value="em"></el-option>
          <el-option label="元素充能效率" value="er"></el-option>
        </el-select>
      </el-col>
      <el-col :span="8">
        <el-select v-model="nowArtifact[1]" placeholder="空之杯" size="medium" @change="setArtifact();countStats()">
          <el-option label="生命值" value="hp"></el-option>
          <el-option label="攻击力" value="atk"></el-option>
          <el-option label="防御力" value="def"></el-option>
          <el-option label="元素精通" value="em"></el-option>
          <el-option label="元素/物理伤害加成" value="ed"></el-option>
        </el-select>
      </el-col>
      <el-col :span="8">
        <el-select v-model="nowArtifact[2]" placeholder="理之冠" size="medium" @change="setArtifact();countStats()">
          <el-option label="生命值" value="hp"></el-option>
          <el-option label="攻击力" value="atk"></el-option>
          <el-option label="防御力" value="def"></el-option>
          <el-option label="元素精通" value="em"></el-option>
          <el-option label="暴击率" value="cr"></el-option>
          <el-option label="暴击伤害" value="cd"></el-option>
          <el-option label="治疗加成" value="hb"></el-option>
        </el-select>
      </el-col>
    </el-row>
    <el-row type="flex" align="middle">
      <el-col :span="4">
        <span>生命值</span>
      </el-col>
      <el-col :span="20">
        <el-input v-model="property[0]" size="medium" clearable @change="countStats()"></el-input>
      </el-col>
    </el-row>
    <el-row type="flex" align="middle">
      <el-col :span="4">
        <span>攻击力</span>
      </el-col>
      <el-col :span="20">
        <el-input v-model="property[1]" size="medium" clearable @change="countStats()"></el-input>
      </el-col>
    </el-row>
    <el-row type="flex" align="middle">
      <el-col :span="4">
        <span>防御力</span>
      </el-col>
      <el-col :span="20">
        <el-input v-model="property[2]" size="medium" clearable @change="countStats()"></el-input>
      </el-col>
    </el-row>
    <el-row type="flex" align="middle">
      <el-col :span="4">
        <span>元素精通</span>
      </el-col>
      <el-col :span="20">
        <el-input v-model="property[3]" size="medium" clearable @change="countStats()"></el-input>
      </el-col>
    </el-row>
    <el-row type="flex" align="middle">
      <el-col :span="4">
        <span>暴击率</span>
      </el-col>
      <el-col :span="20">
        <el-input v-model="property[4]" size="medium" clearable @change="countStats()"></el-input>
      </el-col>
    </el-row>
    <el-row type="flex" align="middle">
      <el-col :span="4">
        <span>暴击伤害</span>
      </el-col>
      <el-col :span="20">
        <el-input v-model="property[5]" size="medium" clearable @change="countStats()"></el-input>
      </el-col>
    </el-row>
    <el-row type="flex" align="middle">
      <el-col :span="4">
        <span>元素充能效率</span>
      </el-col>
      <el-col :span="20">
        <el-input v-model="property[6]" size="medium" clearable @change="countStats()"></el-input>
      </el-col>
    </el-row>
    <el-row :gutter="10">
      <el-col :span="3">
        <span>有效词条</span>
      </el-col>
      <el-col :span="3" offset="1">
        <el-checkbox v-model="isChecked[0]" @change="changeMode()">生命</el-checkbox>
      </el-col>
      <el-col :span="3">
        <el-checkbox v-model="isChecked[1]" @change="changeMode()">攻击</el-checkbox>
      </el-col>
      <el-col :span="3">
        <el-checkbox v-model="isChecked[2]" @change="changeMode()">防御</el-checkbox>
      </el-col>
      <el-col :span="3">
        <el-checkbox v-model="isChecked[3]" @change="changeMode()">精通</el-checkbox>
      </el-col>
      <el-col :span="3">
        <el-checkbox v-model="isChecked[4]" @change="changeMode()">暴击</el-checkbox>
      </el-col>
      <el-col :span="3">
        <el-checkbox v-model="isChecked[5]" @change="changeMode()">暴伤</el-checkbox>
      </el-col>
      <el-col :span="2">
        <el-checkbox v-model="isChecked[6]" @change="changeMode()">充能</el-checkbox>
      </el-col>
    </el-row>
    <div class="show-result" v-html="html"></div>
  </div>
</template>

<script>
export default {
  name: 'MyApp',
  beforeCreate () {
    setTimeout(() => {
      let path = ['character', 'weapon']
      for (let i = 0; path[i]; i++) {
        this.getData(path[i])
      }
    }, 100)
  },
  data () {
    return {
      elementList: [{
        value: 'Pyro',
        label: '火'
      }, {
        value: 'Hydro',
        label: '水'
      }, {
        value: 'Anemo',
        label: '风'
      }, {
        value: 'Electro',
        label: '雷'
      }, {
        value: 'Dendro',
        label: '草'
      }, {
        value: 'Cryo',
        label: '冰'
      }, {
        value: 'Geo',
        label: '岩'
      }],
      levelList: [{
        value: 70,
        label: '70级'
      }, {
        value: 80,
        label: '80级'
      }, {
        value: 90,
        label: '90级'
      }],
      dataList: [{
        character: []
      }, {
        weapon: []
      }],
      targetChar: [],
      targerWeapon: [],
      isChecked: [],
      element: '',
      charName: '',
      weaponName: '',
      level: '',
      weaponATK: '',
      nowArtifact: ['', '', ''],
      recordArtifact: ['atk', 'ed', 'cd'],
      code: 0,
      type: '',
      hp: 0,
      atk: 0,
      def: 0,
      mode: [0, 0, 0, 0, 0, 0, 0],
      property: [0, 0, 0, 0, 0, 0, 0],
      artifact: [0, 1, 0, 0, 0],
      result: [0, 0, 0, 0, 0, 0, 0],
      valid_stats: 0,
      html: '<span> </span>'
    }
  },
  methods: {
    getData (path) {
      this.axios.get(path).then((response) => {
        let data = []
        for (let i = 1; response.data[i]; i++) {
          data.push(response.data[i])
        }
        this.dataList[path] = data
      })
    },
    createTargetChar () {
      this.targetChar = []
      this.charName = ''
      for (var i = 0; i < this.dataList.character.length; i++) {
        if (this.dataList.character[i].element === this.element) {
          this.targetChar.push(this.dataList.character[i])
        }
      }
    },
    createTargetWeapon () {
      this.targerWeapon = []
      for (var i = 0; i < this.dataList.weapon.length; i++) {
        if (this.dataList.weapon[i].type === this.type) {
          this.targerWeapon.push(this.dataList.weapon[i])
        }
      }
      if (this.targerWeapon !== null && this.targerWeapon.length > 2) {
        let n = this.targerWeapon.length
        for (i = 0; i < n; i++) {
          let flag = true
          for (var j = 0; j < n - i - 1; j++) {
            if (this.targerWeapon[j].baseATK < this.targerWeapon[j + 1].baseATK) {
              flag = false
              let temp = this.targerWeapon[j]
              this.targerWeapon[j] = this.targerWeapon[j + 1]
              this.targerWeapon[j + 1] = temp
            }
          }
          if (flag) break
        }
      }
    },
    setChar () {
      for (var i = 0; i < this.dataList.character.length; i++) {
        if (this.dataList.character[i].name === this.charName) {
          this.code = i
          this.type = this.dataList.character[i].type
          this.mode = this.dataList.character[i].mode
          this.weaponName = ''
          this.setProperty()
          break
        }
      }
    },
    setProperty () {
      switch (this.level) {
        case 70:
          this.hp = this.dataList.character[this.code].propertyLv70['baseHP']
          this.atk = this.dataList.character[this.code].propertyLv70['baseATK']
          this.def = this.dataList.character[this.code].propertyLv70['baseDEF']
          break
        case 80:
          this.hp = this.dataList.character[this.code].propertyLv80['baseHP']
          this.atk = this.dataList.character[this.code].propertyLv80['baseATK']
          this.def = this.dataList.character[this.code].propertyLv80['baseDEF']
          break
        case 90:
          this.hp = this.dataList.character[this.code].propertyLv90['baseHP']
          this.atk = this.dataList.character[this.code].propertyLv90['baseATK']
          this.def = this.dataList.character[this.code].propertyLv90['baseDEF']
          break
      }
    },
    setWeapon () {
      for (var i = 0; i < this.dataList.weapon.length; i++) {
        if (this.dataList.weapon[i].name === this.weaponName) {
          this.weaponATK = this.dataList.weapon[i].baseATK
        }
      }
    },
    setStats (event, n) {
      if (event.target.value === '' || event.target.value === null || isNaN(parseFloat(event.target.value))) {
        event.target.value = 0
      }
      switch (n) {
        case 0:
          this.property[n] = parseFloat(event.currentTarget.value)
          break
        case 1:
          this.property[n] = parseFloat(event.currentTarget.value)
          break
        case 2:
          this.property[n] = parseFloat(event.currentTarget.value)
          break
        case 3:
          this.property[n] = parseFloat(event.currentTarget.value)
          break
        case 4:
          this.property[n] = parseFloat(event.currentTarget.value)
          break
        case 5:
          this.property[n] = parseFloat(event.currentTarget.value)
          break
        case 6:
          this.property[n] = parseFloat(event.currentTarget.value)
          break
      }
    },
    setMode () {
      switch (this.dataList.character[this.code].mode) {
        // 生命, 攻击, 防御, 精通, 暴率, 暴伤, 充能
        case 1: // 攻双暴: 通用
          this.mode = [0, 1, 0, 0, 1, 1, 0]
          break
        case 2:
          // 攻精双暴: 增幅通用
          this.mode = [0, 1, 0, 1, 1, 1, 0]
          break
        case 3:
          // 攻充双暴: 莫娜, 琴, 优菈, 雷电将军, 北斗, 罗莎莉亚, 九条裟罗
          this.mode = [0, 1, 0, 0, 1, 1, 1]
          break
        case 4:
          // 攻精充双暴: 旅行者-雷, 温迪, 八重神子, 丽莎, 香菱, 行秋
          this.mode = [0, 1, 0, 1, 1, 1, 1]
          break
        case 5:
          // 攻精充: 早柚
          this.mode = [0, 1, 0, 1, 0, 0, 1]
          break
        case 6:
          // 攻充: 七七, 申鹤
          this.mode = [0, 1, 0, 0, 0, 0, 1]
          break
        case 7:
          // 生攻双暴: 神里绫人
          this.mode = [0.5, 1, 0, 0, 1, 1, 0]
          break
        case 8:
          // 生攻精双暴: 胡桃
          this.mode = [1, 0.4, 0, 1, 1, 1, 0]
          break
        case 9:
          // 生充双暴: 夜兰
          this.mode = [1, 0, 0, 0, 1, 1, 1]
          break
        case 10:
          // 生攻充: 珊瑚宫心海
          this.mode = [1, 0.4, 0, 0, 0, 0, 1]
          break
        case 11:
          // 生精: 久岐忍
          this.mode = [1, 0, 0, 1, 0, 0, 0]
          break
        case 12:
        // 生充: 钟离, 班尼特, 芭芭拉, 迪奥娜, 托马
          this.mode = [1, 0, 0, 0, 0, 0, 1]
          break
        case 13:
          // 攻防充双暴: 荒泷一斗
          this.mode = [0, 0.4, 1, 0, 1, 1, 1]
          break
        case 14:
          // 防充双暴: 诺艾尔
          this.mode = [0, 0, 1, 0, 1, 1, 1]
          break
        case 15:
          // 防双暴: 阿贝多
          this.mode = [0, 0, 1, 0, 1, 1, 0]
          break
        case 16:
          // 防充: 辛焱, 五郎, 云堇
          this.mode = [0, 0, 1, 0, 0, 0, 1]
          break
        case 17:
          // 精充: 旅行者-风, 枫原万叶, 砂糖
          this.mode = [0, 0, 0, 1, 0, 0, 1]
          break
      }
      this.setCheckbox()
    },
    setArtifact () {
      for (var i = 0; i < 3; i++) {
        if (this.nowArtifact[i] !== this.recordArtifact[i]) {
          this.subArtifact(this.recordArtifact[i])
          this.addArtifact(this.nowArtifact[i])
          this.recordArtifact[i] = this.nowArtifact[i]
          break
        }
      }
    },
    setCheckbox () {
      for (var i = 0; i < this.mode.length; i++) {
        if (this.mode[i] > 0) {
          this.isChecked[i] = true
        } else {
          this.isChecked[i] = false
        }
      }
    },
    changeMode () {
      for (var i = 0; i < this.isChecked.length; i++) {
        if (this.isChecked[i]) {
          this.mode[i] = 1
        } else {
          this.mode[i] = 0
        }
      }
      this.addStats()
    },
    countStats () {
      if (this.charName === '' || this.level === '' || this.weaponATK === '' || this.nowArtifact[0] === '' || this.nowArtifact[1] === '' || this.nowArtifact[2] === '') {
        return null
      }
      this.result[0] = (((this.property[0] - 4780) / this.hp) - this.artifact[0] * 0.464) / 0.05
      this.result[1] = ((this.property[1] - 311) / (this.atk + this.weaponATK) - this.artifact[1] * 0.464) / 0.05
      this.result[2] = ((this.property[2] / this.def) - this.artifact[2] * 0.583) / 0.062
      this.result[3] = (this.property[3] - this.artifact[3] * 187) / 20
      this.result[4] = (this.property[4] - 31.3) / 3.3
      this.result[5] = this.property[5] / 6.6
      this.result[6] = (this.property[6] - this.artifact[4] * 51.8) / 5
      for (var i = 0; i < this.result.length; i++) {
        this.result[i].toFixed(1)
      }
      this.addStats()
    },
    addStats () {
      this.valid_stats = 0
      for (var i = 0; i < this.result.length; i++) {
        if (this.result[i] < 0) {
          this.result[i] = 0
        }
        this.valid_stats += this.result[i] * this.mode[i]
      }
      this.html = '<span>共 ' + this.valid_stats.toFixed(1) + ' 词条</span>'
    },
    addArtifact (piece) {
      switch (piece) {
        case 'hp':
          this.artifact[0]++
          break
        case 'atk':
          this.artifact[1]++
          break
        case 'def':
          this.artifact[2]++
          break
        case 'em':
          this.artifact[3]++
          break
        case 'er':
          this.artifact[4]++
      }
    },
    subArtifact (piece) {
      switch (piece) {
        case 'hp':
          this.artifact[0]--
          break
        case 'atk':
          this.artifact[1]--
          break
        case 'def':
          this.artifact[2]--
          break
        case 'em':
          this.artifact[3]--
          break
        case 'er':
          this.artifact[4]--
      }
    }
  }
}
</script>

<style scoped>
#content-box {
  width: 760px;
  margin: auto;
}

.el-row {
    margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}

.el-select {
  border-color: #deb37c;
}

.show-result {
  width: 120px;
  margin: auto;
  text-align: center;
}
</style>
