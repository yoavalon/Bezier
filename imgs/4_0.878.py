d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.E, Length.medium)

d.end()
