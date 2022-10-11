d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)

d.end()
