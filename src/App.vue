<template>
  <v-app id="app">

    <!-- sidebar -->
    <v-navigation-drawer
        v-model="sidebar"
        dark color="indego"
        fixed
        app>
      <v-list>
        <v-list-tile
          v-for="item in menuItems"
          v-bind:key="item.title"
          v-bind:to="item.path">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>{{ item.title }}</v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <!-- toolbar -->
    <v-toolbar dark color="indigo" fixed app>

      <v-toolbar-side-icon @click="sidebar = !sidebar">
      </v-toolbar-side-icon>

        <v-toolbar-title>
          <router-link to="/" tag="span" style="cursor: pointer">
            {{ appTitle }}
          </router-link>
        </v-toolbar-title>
      <v-spacer></v-spacer>

        <v-toolbar-items class="hidden-xs-only">
          <v-btn
            flat
            v-for="item in menuItems"
            :key="item.title"
            :to="item.path">
            <v-icon left dark>{{ item.icon }}</v-icon>
            {{ item.title }}
          </v-btn>
        </v-toolbar-items>

    </v-toolbar>

    <!-- content -->
    <v-content>
      <v-container fluid >
        <v-layout
          justify-center
          align-center
        >
          <v-flex text-xs-center>
            <router-view></router-view>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>

    <v-footer color="indigo" app>
      <span class="white--text">&copy; 2018</span>
    </v-footer>

  </v-app>
</template>

<script>
export default {
  data () {
    return {
      appTitle: 'My App',
      sidebar: false,
      menuItems: [
        { title: 'Home', path: '/home', icon: 'home' },
        { title: 'Api', path: '/api', icon: 'apps' }
      ]
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#plus {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 50px;
  vertical-align: top;
  line-height: 100px;
}
#logo {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 60px;
  color: purple;
  vertical-align: top;
  line-height: 100px;
}
</style>
