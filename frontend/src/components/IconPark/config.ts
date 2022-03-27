import type { App } from 'vue'
import { User, Lock, Unlock, ExpandRight, ExpandLeft, Home } from '@icon-park/vue-next'

export const useIconPark = (app: App) => {
  app.component('IconParkUser', User)
  app.component('IconParkLock', Lock)
  app.component('IconParkUnlock', Unlock)
  app.component('IconParkExpandRight', ExpandRight)
  app.component('IconParkExpandLeft', ExpandLeft)
  app.component('IconParkHome', Home)
}