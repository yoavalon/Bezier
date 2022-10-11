d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
