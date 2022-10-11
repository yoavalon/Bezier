d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.E, Length.medium)

d.end()
