export const getFeatureConfig = (permissions = []) => {
  const allButtons = [
    {
      key: 'accessDatabase',
      label: 'دسترسی به پایگاه داده',
      route: '/access_db',
      permission: 'access_db'
    },
    {
      key: 'manageData',
      label: 'اکسپورت داده',
      route: '/manage_data',
      permission: 'manage_data'
    },
    {
      key: 'viewReports',
      label: 'گزارش و تاریخچه',
      route: '/logs',
      permission: 'view_logs'
    },
    {
      key: 'accessKnowledgeBase',
      label: 'دسترسی به پایگاه دانش',
      route: '/access_kb',
      permission: 'access_kb'
    }
  ]

  return {
    buttons: allButtons.filter(btn => permissions.includes(btn.permission))
  }
}
