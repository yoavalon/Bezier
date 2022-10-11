d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(0,1)

d.end()
