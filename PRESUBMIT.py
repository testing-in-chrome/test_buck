def CheckChange(input_api, output_api):
  results = []
  results.extend(
      input_api.canned_checks.CheckDoNotSubmit(input_api, output_api))
  results.extend(
      input_api.canned_checks.CheckChangeHasNoTabs(input_api, output_api))
  results.extend(
      input_api.canned_checks.CheckLongLines(input_api, output_api, 80))
  results.extend(input_api.canned_checks.CheckOwners(input_api, output_api))
  # Require a BUG= line and a HOW_TO_TEST= line.
  if not input_api.change.BUG or not input_api.change.TEST:
    results.extend([output_api.PresubmitError(
        'Must provide a BUG= line and a TEST line.')])
  if input_api.change.BUG and not input_api.change.BUG.startswith('#'):
    results.extend([output_api.PresubmitError('BUG= must start with "#".')])
  return results

def CheckChangeOnUpload(input_api, output_api):
  return CheckChange(input_api, output_api)

def CheckChangeOnCommit(input_api, output_api):
   return CheckChange(input_api, output_api)
