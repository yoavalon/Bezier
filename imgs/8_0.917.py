d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,3)

d.end()
