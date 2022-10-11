d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
