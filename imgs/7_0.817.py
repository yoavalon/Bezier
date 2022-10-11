d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)

d.end()
