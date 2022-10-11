d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(0,3)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
