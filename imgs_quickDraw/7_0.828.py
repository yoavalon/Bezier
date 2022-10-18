d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,0)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)

d.end()
